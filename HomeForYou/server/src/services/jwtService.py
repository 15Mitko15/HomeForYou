import jwt
from datetime import datetime, timedelta, timezone
from typing import Dict, Any
from fastapi import HTTPException
from src.config import JWT_SECRET


class JWTService:
    """Handles JWT creation and verification"""

    def sign(self, payload: Dict[str, Any]) -> str:
        """Generates a JWT token"""
        try:
            expiration = datetime.now(timezone.utc) + timedelta(hours=1)
            payload["exp"] = expiration
            token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
            return token
        except Exception:
            raise HTTPException(status_code=500, detail="Error creating JWT token")

    def verify(self, token: str) -> Dict[str, Any]:
        """Verifies the JWT token"""
        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")


jwt_service = JWTService()
