


#ifndef TF_MINMAX_H
#define TF_MINMAX_H

template <class T>
TFSIMD_FORCE_INLINE const T& tfMin(const T& a, const T& b) 
{
  return a < b ? a : b ;
}

template <class T>
TFSIMD_FORCE_INLINE const T& tfMax(const T& a, const T& b) 
{
  return  a > b ? a : b;
}


template <class T>
TFSIMD_FORCE_INLINE void tfSetMin(T& a, const T& b) 
{
    if (b < a) 
	{
		a = b;
	}
}

template <class T>
TFSIMD_FORCE_INLINE void tfSetMax(T& a, const T& b) 
{
    if (a < b) 
	{
		a = b;
	}
}


#endif