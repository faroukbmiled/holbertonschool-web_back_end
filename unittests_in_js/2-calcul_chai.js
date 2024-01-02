const SUM = 'SUM';
const SUBTRACT = 'SUBTRACT';
const DIVIDE = 'DIVIDE';

function isNegZero(n) {
  n = Number(n);
  return n === 0 && 1 / n === -Infinity;
}

module.exports = function calculateNumber(type, a, b = 0) {
  let numA = Number(a);
  let numB = Number(b);

  if (Number.isNaN(numA) || Number.isNaN(numB))
    throw TypeError('Parameters must be numbers or able to coerce to number');

  numA = Math.round(numA);
  numB = Math.round(numB);

  switch (type) {
    case SUM:
      return numA + numB;
    case SUBTRACT:
      return numA - numB;
    case DIVIDE:
      if (numB === 0) return 'ERROR';
      const quotient = numA / numB;
      return isNegZero(quotient) ? 0 : quotient;
    default:
      throw Error(
        'Invalid operation type. Valid types are "SUM", "SUBTRACT", and "DIVIDE".'
      );
  }
};