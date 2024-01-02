const Utils = {
  isNegZero(n) {
    const num = Number(n);
    return num === 0 && 1 / num === -Infinity;
  },
  calculateNumber(type, a, b = 0) {
    let numA = Number(a);
    let numB = Number(b);

    if (Number.isNaN(numA) || Number.isNaN(numB))
      throw TypeError('Parameters must be numbers or able to coerce to number');

    numA = Math.round(numA);
    numB = Math.round(numB);

    let quotient;

    switch (type) {
      case 'SUM':
        return numA + numB;
      case 'SUBTRACT':
        return numA - numB;
      case 'DIVIDE':
        if (numB === 0) return 'ERROR';
        quotient = numA / numB;
        return this.isNegZero(quotient) ? 0 : quotient;
      default:
        throw Error(
          'Invalid operation type. Valid types are "SUM", "SUBTRACT", and "DIVIDE".'
        );
    }
  }
};

module.exports = Utils;
