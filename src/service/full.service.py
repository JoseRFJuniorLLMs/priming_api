from typing import List
from bson import ObjectId
import re

from .mongodb_model import db
from .OID import OID
from .StatusConverter import StatusConverter
from .Status import Status
from .PrimeCoin import PrimeCoin
from .PrimeTargetCollection import PrimeTargetCollection
from .PrimeTargetDictionaryCollection import PrimeTargetDictionaryCollection
from .PrimeTargetPhraseCollection import PrimeTargetPhraseCollection
from .PrimeTargetTextCollection import PrimeTargetTextCollection
from .PrimeTargetYoutubeCollection import PrimeTargetYoutubeCollection
from .ClassroomCollection import ClassroomCollection
from .CourseCollection import CourseCollection
from .LessonCollection import LessonCollection
from .ModuleCollection import ModuleCollection
from .ProfessorCollection import ProfessorCollection
from .StudentCollection import StudentCollection


def create_primecoin(primecoin_data: PrimeCoin):
    return db().save_document(collection="PrimeCoinCollection", document=primecoin_data.mongo())


def update_primecoin(primecoin_data: PrimeCoin):
    db().update_document(
        collection="PrimeCoinCollection",
        key={"_id": primecoin_data.id},
        document=primecoin_data.mongo(),
    )


def delete_primecoin_by_id(primecoin_id: str):
    db().delete_by_key(collection="PrimeCoinCollection", key={"_id": ObjectId(primecoin_id)})


def get_list_primecoins():
    list_primecoins = db().get_by_filter(collection="PrimeCoinCollection", key={})
    return [PrimeCoin.from_mongo(primecoin) for primecoin in list_primecoins]


def get_primecoin_by_id(primecoin_id: str):
    result = db().get_by_key(collection="PrimeCoinCollection", key={"_id": ObjectId(primecoin_id)})
    return PrimeCoin.from_mongo(result)


def create_primetarget(primetarget_data: PrimeTargetCollection):
    return db().save_document(collection="PrimeTargetCollection", document=primetarget_data.mongo())


def update_primetarget(primetarget_data: PrimeTargetCollection):
    db().update_document(
        collection="PrimeTargetCollection",
        key={"_id": primetarget_data.id},
        document=primetarget_data.mongo(),
    )


def delete_primetarget_by_id(primetarget_id: str):
    db().delete_by_key(collection="PrimeTargetCollection", key={"_id": ObjectId(primetarget_id)})


def get_list_primetargets():
    list_primetargets = db().get_by_filter(collection="PrimeTargetCollection", key={})
    return [PrimeTargetCollection.from_mongo(primetarget) for primetarget in list_primetargets]


def get_primetarget_by_id(primetarget_id: str):
    result = db().get_by_key(collection="PrimeTargetCollection", key={"_id": ObjectId(primetarget_id)})
    return PrimeTargetCollection.from_mongo(result)

def create_primetargetdictionary(primetargetdictionary_data: PrimeTargetDictionaryCollection):
    return db().save_document(collection="PrimeTargetDictionaryCollection", document=primetargetdictionary_data.mongo())


def update_primetargetdictionary(primetargetdictionary_data: PrimeTargetDictionaryCollection):
    db().update_document(
        collection="PrimeTargetDictionaryCollection",
        key={"_id": primetargetdictionary_data.id},
        document=primetargetdictionary_data.mongo(),
    )


def delete_primetargetdictionary_by_id(primetargetdictionary_id: str):
    db().delete_by_key(collection="PrimeTargetDictionaryCollection", key={"_id": ObjectId(primetargetdictionary_id)})


def get_list_primetargetdictionaries():
    list_primetargetdictionaries = db().get_by_filter(collection="PrimeTargetDictionaryCollection", key={})
    return [PrimeTargetDictionaryCollection.from_mongo(primetargetdictionary) for primetargetdictionary in list_primetargetdictionaries]


def get_primetargetdictionary_by_id(primetargetdictionary_id: str):
    result = db().get_by_key(collection="PrimeTargetDictionaryCollection", key={"_id": ObjectId(primetargetdictionary_id)})
    return PrimeTargetDictionaryCollection.from_mongo(result)


def create_primetargetphrase(primetargetphrase_data: PrimeTargetPhraseCollection):
    return db().save_document(collection="PrimeTargetPhraseCollection", document=primetargetphrase_data.mongo())


def update_primetargetphrase(primetargetphrase_data: PrimeTargetPhraseCollection):
    db().update_document(
        collection="PrimeTargetPhraseCollection",
        key={"_id": primetargetphrase_data.id},
        document=primetargetphrase_data.mongo(),
    )


def delete_primetargetphrase_by_id(primetargetphrase_id: str):
    db().delete_by_key(collection="PrimeTargetPhraseCollection", key={"_id": ObjectId(primetargetphrase_id)})


def get_list_primetargetphrases():
    list_primetargetphrases = db().get_by_filter(collection="PrimeTargetPhraseCollection", key={})
    return [PrimeTargetPhraseCollection.from_mongo(primetargetphrase) for primetargetphrase in list_primetargetphrases]


def get_primetargetphrase_by_id(primetargetphrase_id: str):
    result = db().get_by_key(collection="PrimeTargetPhraseCollection", key={"_id": ObjectId(primetargetphrase_id)})
    return PrimeTargetPhraseCollection.from_mongo(result)


def create_primetargettext(primetargettext_data: PrimeTargetTextCollection):
    return db().save_document(collection="PrimeTargetTextCollection", document=primetargettext_data.mongo())


def update_primetargettext(primetargettext_data: PrimeTargetTextCollection):
    db().update_document(
        collection="PrimeTargetTextCollection",
        key={"_id": primetargettext_data.id},
        document=primetargettext_data.mongo(),
    )


def delete_primetargettext_by_id(primetargettext_id: str):
    db().delete_by_key(collection="PrimeTargetTextCollection", key={"_id": ObjectId(primetargettext_id)})


def get_list_primetargettexts():
    list_primetargettexts = db().get_by_filter(collection="PrimeTargetTextCollection", key={})
    return [PrimeTargetTextCollection.from_mongo(primetargettext) for primetargettext in list_primetargettexts]


def get_primetargettext_by_id(primetargettext_id: str):
    result = db().get_by_key(collection="PrimeTargetTextCollection", key={"_id": ObjectId(primetargettext_id)})
    return PrimeTargetTextCollection.from_mongo(result)


def create_primetargetyoutube(primetargetyoutube_data: PrimeTargetYoutubeCollection):
    return db().save_document(collection="PrimeTargetYoutubeCollection", document=primetargetyoutube_data.mongo())


def update_primetargetyoutube(primetargetyoutube_data: PrimeTargetYoutubeCollection):
    db().update_document(
        collection="PrimeTargetYoutubeCollection",
        key={"_id": primetargetyoutube_data.id},
        document=primetargetyoutube_data.mongo(),
    )


def delete_primetargetyoutube_by_id(primetargetyoutube_id: str):
    db().delete_by_key(collection="PrimeTargetYoutubeCollection", key={"_id": ObjectId(primetargetyoutube_id)})


def get_list_primetargetyoutubes():
    list_primetargetyoutubes = db().get_by_filter(collection="PrimeTargetYoutubeCollection", key={})
    return [PrimeTargetYoutubeCollection.from_mongo(primetargetyoutube) for primetargetyoutube in list_primetargetyoutubes]


def get_primetargetyoutube_by_id(primetargetyoutube_id: str):
    result = db().get_by_key(collection="PrimeTargetYoutubeCollection", key={"_id": ObjectId(primetargetyoutube_id)})
    return PrimeTargetYoutubeCollection.from_mongo(result)


def create_classroom(classroom_data: ClassroomCollection):
    return db().save_document(collection="ClassroomCollection", document=classroom_data.mongo())


def update_classroom(classroom_data: ClassroomCollection):
    db().update_document(
        collection="ClassroomCollection",
        key={"_id": classroom_data.id},
        document=classroom_data.mongo(),
    )


def delete_classroom_by_id(classroom_id: str):
    db().delete_by_key(collection="ClassroomCollection", key={"_id": ObjectId(classroom_id)})


def get_list_classrooms():
    list_classrooms = db().get_by_filter(collection="ClassroomCollection", key={})
    return [ClassroomCollection.from_mongo(classroom) for classroom in list_classrooms]


def get_classroom_by_id(classroom_id: str):
    result = db().get_by_key(collection="ClassroomCollection", key={"_id": ObjectId(classroom_id)})
    return ClassroomCollection.from_mongo(result)


def create_course(course_data: CourseCollection):
    return db().save_document(collection="CourseCollection", document=course_data.mongo())


def update_course(course_data: CourseCollection):
    db().update_document(
        collection="CourseCollection",
        key={"_id": course_data.id},
        document=course_data.mongo(),
    )


def delete_course_by_id(course_id: str):
    db().delete_by_key(collection="CourseCollection", key={"_id": ObjectId(course_id)})


def get_list_courses():
    list_courses = db().get_by_filter(collection="CourseCollection", key={})
    return [CourseCollection.from_mongo(course) for course in list_courses]


def get_course_by_id(course_id: str):
    result = db().get_by_key(collection="CourseCollection", key={"_id": ObjectId(course_id)})
    return CourseCollection.from_mongo(result)


def create_lesson(lesson_data: LessonCollection):
    return db().save_document(collection="LessonCollection", document=lesson_data.mongo())


def update_lesson(lesson_data: LessonCollection):
    db().update_document(
        collection="LessonCollection",
        key={"_id": lesson_data.id},
        document=lesson_data.mongo(),
    )


def delete_lesson_by_id(lesson_id: str):
    db().delete_by_key(collection="LessonCollection", key={"_id": ObjectId(lesson_id)})


def get_list_lessons():
    list_lessons = db().get_by_filter(collection="LessonCollection", key={})
    return [LessonCollection.from_mongo(lesson) for lesson in list_lessons]


def get_lesson_by_id(lesson_id: str):
    result = db().get_by_key(collection="LessonCollection", key={"_id": ObjectId(lesson_id)})
    return LessonCollection.from_mongo(result)


def create_module(module_data: ModuleCollection):
    return db().save_document(collection="ModuleCollection", document=module_data.mongo())


def update_module(module_data: ModuleCollection):
    db().update_document(
        collection="ModuleCollection",
        key={"_id": module_data.id},
        document=module_data.mongo(),
    )


def delete_module_by_id(module_id: str):
    db().delete_by_key(collection="ModuleCollection", key={"_id": ObjectId(module_id)})


def get_list_modules():
    list_modules = db().get_by_filter(collection="ModuleCollection", key={})
    return [ModuleCollection.from_mongo(module) for module in list_modules]


def get_module_by_id(module_id: str):
    result = db().get_by_key(collection="ModuleCollection", key={"_id": ObjectId(module_id)})
    return ModuleCollection.from_mongo(result)


def create_professor(professor_data: ProfessorCollection):
    return db().save_document(collection="ProfessorCollection", document=professor_data.mongo())


def update_professor(professor_data: ProfessorCollection):
    db().update_document(
        collection="ProfessorCollection",
        key={"_id": professor_data.id},
        document=professor_data.mongo(),
    )


def delete_professor_by_id(professor_id: str):
    db().delete_by_key(collection="ProfessorCollection", key={"_id": ObjectId(professor_id)})


def get_list_professors():
    list_professors = db().get_by_filter(collection="ProfessorCollection", key={})
    return [ProfessorCollection.from_mongo(professor) for professor in list_professors]


def get_professor_by_id(professor_id: str):
    result = db().get_by_key(collection="ProfessorCollection", key={"_id": ObjectId(professor_id)})
    return ProfessorCollection.from_mongo(result)


def create_student(student_data: StudentCollection):
    return db().save_document(collection="StudentCollection", document=student_data.mongo())


def update_student(student_data: StudentCollection):
    db().update_document(
        collection="StudentCollection",
        key={"_id": student_data.id},
        document=student_data.mongo(),
    )


def delete_student_by_id(student_id: str):
    db().delete_by_key(collection="StudentCollection", key={"_id": ObjectId(student_id)})


def get_list_students():
    list_students = db().get_by_filter(collection="StudentCollection", key={})
    return [StudentCollection.from_mongo(student) for student in list_students]


def get_student_by_id(student_id: str):
    result = db().get_by_key(collection="StudentCollection", key={"_id": ObjectId(student_id)})
    return StudentCollection.from_mongo(result)

