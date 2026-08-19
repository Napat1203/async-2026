import asyncio
from typing import Dict, List 
from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

STUDENTS = ["6710301034","6710301033","6710301043","6710301019","6710301020","6710301017"]
GROUP_SIZE = len(STUDENTS)
TOTAL_COUPONS = (GROUP_SIZE * 2) - 1 

coupons_db: List[str] = [f"COUPONS-{i:02d}" for i in range(1, TOTAL_COUPONS + 1)] 

current_coupon_index = 0 

student_claims: Dict[str, List[str]] = {student_id: [] for student_id in STUDENTS }

class ClaimRequest(BaseModel):
    student_id: str 

@app.post("/claim")
async def claim_coupon(req: ClaimRequest):
    global current_coupon_index 
    student_id = req.student_id 

    if student_id not in student_claims:
        return {"status": "INVALID_STUDENT", "message": "ไม่พบรายชื่อในระบบ"}

    if len(student_claims[student_id]) >= 2:
        return {"status": "LIMIT_REACHED", "message": "คุณรับคูปองครบ 2 ใบแล้ว"} 

    # Don't have Lock 
    if current_coupon_index < len(coupons_db):
        index_to_claim = current_coupon_index 
        await asyncio.sleep(0.1)

        coupon = coupons_db[index_to_claim]
        student_claims[student_id].append(coupon) 

        current_coupon_index = index_to_claim + 1

        return {"status": "SUCCESS", "claimed_coupon": coupon, "total_owned": len(student_claims[student_id])}

    return {"status": "OUT_OF_STOCK", "message": "คูปองหมดแล้ว"} 

@app.get("/summary")
async def get_summary():
    return {
        "remaing_stock": len(coupons_db) - current_coupon_index,
        "student_claims": student_claims
    }
