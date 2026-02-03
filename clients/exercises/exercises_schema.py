from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    maxScore: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа списков упражнений.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа упражнения.
    """
    exercise: ExerciseSchema


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнения.
    """
    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание стьруктуры ответа на обновление упражнения
    """
    exercise: ExerciseSchema
