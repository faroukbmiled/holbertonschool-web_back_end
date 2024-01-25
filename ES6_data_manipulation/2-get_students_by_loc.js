export default function getStudentsByLocation(list, city) {
  return list.filter((l) => l.location === city);
}
