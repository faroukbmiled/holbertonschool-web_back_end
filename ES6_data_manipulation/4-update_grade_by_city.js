function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const foundGrade = newGrades.filter(
        (newGrade) => newGrade.studentId === student.id,
      );

      const grade = foundGrade[0] ? foundGrade[0].grade : 'N/A';

      return {
        ...student,
        grade,
      };
    });
}

export default updateStudentGradeByCity;
