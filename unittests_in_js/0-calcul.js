module.exports = function calculateNumber(a, b = 0) {
  const numA = Number(a);
  const numB = Number(b);

  if (Number.isNaN(numA) || Number.isNaN(numB))
    throw TypeError('Parameters must be numbers');

    return Math.round(numA) + Math.round(numB);
  };
