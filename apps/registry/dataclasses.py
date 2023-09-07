from dataclasses import dataclass

@dataclass
class MediatorTraining:
    """Класс данных подготовки медиатора."""
    type_code: str
    institution_title: str
    education_course_title: str
    hours: int
    year: int
    certificate_url: str
