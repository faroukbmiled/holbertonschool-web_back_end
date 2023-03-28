function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const foundGrade = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: foundGrade ? foundGrade.grade : "N/A",
      };
    });
}

export default updateStudentGradeByCity;
