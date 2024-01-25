export default function getStudentsByLocation(list) {
  return list.reduce((accumulator, n) => accumulator + n.id, 0);
}
