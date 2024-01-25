export default function cleanSet(set, startString) {
  if (typeof startString === "undefined") {
    return "";
  }
  const filteredValues = Array.from(set)
    .filter((value) => typeof value !== "undefined" && value.startsWith(startString))
    .map((value) => value.slice(startString.length));
  return filteredValues.join("-");
}
