from pydantic import BaseModel

__all__ = [
    "LoanLine"
]


class LoanLine(BaseModel):
    """
    Represents the information contained in a checkout line for a loan receipt.
    """

    loan_reference: str
    document_id: str

    def __hash__(self) -> int:
        return hash(self.loan_line_identifier)

    def __eq__(self, other) -> bool:
        if isinstance(other, LoanLine):
            return other.loan_reference == self.loan_line_identifier
        return False

    @property
    def loan_line_identifier(self) -> str:
        return "//--//".join([self.loan_reference, self.document_id])
