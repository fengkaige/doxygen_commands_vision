



class Test_func_1:
    """!
    \brief Test doxygen.
    """
    def __init__(self):
        """!
        """
        pass
    def test(a, b):
        """!
        test函数描述

        \parblock
        \par 代码块
        \code
        这是一段<b>粗体</b><em>斜体</em>
        \endcode
        \endparblock

        \parblock
        \par效果
        这是一段<b>粗体</b><em>斜体</em>
        \endparblock

		----------

        \parblock
        \par 代码块
        \code
        \parblock
            item-description:\n
            \arg \c AlignLeft left alignment.
            \arg \c AlignCenter center alignment.
            \arg \c AlignRight right alignment
        \endparblock
        \endcode
        \endparblock

        \parblock
        \par 效果
        \parblock
            item-description:\n
            \arg \c AlignLeft left alignment.
            \arg \c AlignCenter center alignment.
            \arg \c AlignRight right alignment
        \endparblock
        \endparblock

		----------

        \parblock
        \par 代码块
        \code
        行内公式:
        The distance between \f$(x_1,y_1)\f$ and \f$(x_2,y_2)\f$ is \f$\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\f$.\n
        独行公式:
        \f[
            c = \sqrt{a^{2}+b_{0}^{2}+e^{x}}
        \f]
        \endcode
        \endparblock

        \parblock
        \par 效果
        行内公式:
        The distance between \f$(x_1,y_1)\f$ and \f$(x_2,y_2)\f$ is \f$\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\f$.\\

        独行公式:
        \f[
            c = \sqrt{a^{2}+b_{0}^{2}+e^{x}}
        \f]
        \endparblock

		----------

        \parblock
        \par 代码块
        \\code{.py}\n
        class Python:\n
            pass\n
        \\endcode\n
        \\code{.cpp}\n
        class Cpp {};\n
        \\endcode\n
        \endparblock

        \parblock
        \par 效果
        \code{.py}
        class Python:
            pass
        \endcode
        \code{.cpp}
        class Cpp {};
        \endcode
        \endparblock

		----------

        \parblock
        \par 代码块
        \code
        \par
            All commands are not disabled in a verbatim block.
            参数格式:\n \param '['x']'  { parameter description }
        \endpar
        \endcode
        \endparblock

        \parblock
        \par 效果
        \par
            All commands are not disabled in a verbatim block.
            参数格式:\n \param '['x']'  { parameter description }
        \endpar
        \endparblock

		----------

        \parblock
        \par 代码块
        \code
        \param [x] first input.
        \param [y] seconde input.
        \endcode
        \endparblock

        \parblock
        \par 效果
        \param [x] first input.
        \param [y] seconde input.
        \endparblock

		----------

        \parblock
        \par 代码块
        \code
        \returns absolute value of \a x.
        \retval output the value of a+b.
        \endcode
        \endparblock

        \parblock
        \par 效果
        \returns absolute value of \a x.
        \retval output the value of a+b.
        \endparblock

		----------

        \parblock
        \par 代码块
        \code
        \note
        This note consists of two paragraphs.
        This is the first paragraph.
        \warning
        This note consists of two paragraphs.
        This is the first paragraph.
        \endcode
        \endparblock

        \parblock
        \par 效果
        \note
        This note consists of two paragraphs.
        This is the first paragraph.

        \warning
        This note consists of two paragraphs.
        This is the first paragraph.
        \endparblock
        """
        return a+b
    def test_language():
        """!
        \parblock
        \par 代码块
        设置不同的输出语言，会有不同输出
        \code
        \~chinese chinese output.
        \~english english output.
        \endcode
        \endparblock

        \parblock
        \par效果
        \~chinese chinese output.
        \~english english output.
        \endparblock
        """
        pass
