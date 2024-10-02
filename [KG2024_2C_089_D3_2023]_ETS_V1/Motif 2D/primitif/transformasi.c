#include math
#include "graphics.h"

typedef float Matrix3x3[3][3];
Matrix3x3 theMatrix;

void matrix3x3SetIdentity(Matrix3x3 m){
	int i, j
	for (i=0; i<3; i++){
		for(j=0; j<3; j++){
			m[i][j] = (i==j);
		}
	}
}

void matrix3x3PreMultiply(Matrix3x3 a, Matrix3x3 b){
	int r,c;
	Matrix3x3 tmp;

	for(r=0;r<3;r++){
		for(c=0;c<3;c++){
			tmp[r][c] = (
				a[r][0]*b[0][c]
				+ a[r][1]*b[1][c]
				+ a[r][2]*b[2][c]
				);
		}
	}

	for (r=0;r<3;r++){
		for(c=0;c<3;c++){
			b[r][c] = tmp[r][c];
		}
	}
}

void translate2D(int tx, int ty){
	Matrix3x3 m;
	matrix3x3SetIdentity(m);
	m[0][2] = tx;
	m[1][2] = ty;
	matrix3x3PreMultiply(m, theMatrix);
}

void scale2D(int sx, int sy, wcPt2 refpt){
	Matrix3x3 m;
	matrix3x3SetIdentity(m);
	m[0][0] = sx;
	m[0][2] = (1-sx)*refpt.x;
	m[1][1] = sy ;
	m[1][2] = (1-sy)*refpt.y;
	matrix3x3PreMultiply(m, theMatrix);
}

void rotate2D(float a, wcPt2 refpt){
	Matrix3x3 m;
	matrix3x3SetIdentity(m);
	a = pToRadians(a);
	m[0][0] = cos(a);
	m[0][1] = - sin(a);
	m[0][2] = refpt.x * (1 - cos(a)) + refpt.y * sin(a);
	m[1][0] = sin(a);
	m[1][1] = cos(a);
	m[1][2] = refpt.y * (1 - cos(a)) - refpt.x * sin(a);
	matrix3x3PreMultiply(m, theMatrix);
}

void transformPoints2D(int npts, wcPt2 *pts){
	int k;
	float tmp;

	for(k = 0;k < npts; k++){
		tmp = theMatrix[0][0] * pts[k].x + theMatrix[0][1] * pts[k].y + theMatrix[0][2];
		pts[k].y = theMatrix[1][0] * pts[k].x + theMatrix[1][1] * pts[k].y + theMatrix[1][2];
		pts[k].x = tmp;
	}
}