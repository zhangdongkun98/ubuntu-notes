#include <iostream>

// extern "C"{
    #include <cblas.h>
// }


// try {
    // #include <cblas.h>
// } catch {
//     std::cout << "here" std::endl;
// }



int main() {
    const int m = 4;  //A的行数，C的行数
    const int n = 2;  //B的列数，C的列数
    const int k = 3;  //A的列数，B的行数
    const float alpha = 1;
    const float beta = 0;
    const int lda = k;  //A的列
    const int ldb = n;  //B的列
    const int ldc = n;  //C的列
    const float A[m * k] = {1, 2, 3,
                            1, 2, 3,
                            1, 2, 3,
                            1, 2, 3};
    const float B[k * n] = {2, 1,
                            2, 1,
                            2, 1};
    float C[m * n];

    int run_time = 0;
    clock_t s = clock();
    while (run_time <  1000000) {
        cblas_sgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
                    m, n, k, alpha, A, lda, B, ldb, beta, C, ldc);
        ++run_time;
    }
    clock_t e = clock();
    std::cout << "OpenBLAS_time: "
              << (e - s) * 1.0 / CLOCKS_PER_SEC
              << " s" << std::endl;

    return 0;
}
