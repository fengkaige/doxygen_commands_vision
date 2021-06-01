



class Test_func_2:
    """!
    \brief Test doxygen.
    """
    def __init__(self):
        """!
        初始化函数
        """
        pass
    def test(a, b):
        """!
        \brief     演示函数1
        \details   第一种风格
        \author    kg
        \version   0.1a
        \date      2021-05
        \pre       First initialize the system.
        \bug       无
        \warning   警告信息
        \copyright GNU Public License.
        pass
        """
    def test_2(x, y):
        """!
        \brief      函数2
        \parblock
            formula:
            \f[
                c = \sqrt{a^{2}+b_{0}^{2}+e^{x}}
            \f]
        \endparblock

        \param [x] first input.
        \param [y] seconde input.

        \returns absolute value of \a x.
        \retval [output] the value of a+b.

        \note
        This note consists of two paragraphs.
        This is the first paragraph.

        \warning
        This note consists of two paragraphs.
        This is the first paragraph.

        \parblock
        \par Example
        \code{.py}
        class Python:
            pass
        \endcode
        \endparblock
        """
        return a+b
    def test_2():
        """!
        \brief      函数2
        \parblock
            行内公式:\n
            The distance between \f$(x_1,y_1)\f$ and \f$(x_2,y_2)\f$ is \f$\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\f$.\n

            item-description:\n
            \arg \c AlignLeft left alignment.
            \arg \c AlignCenter center alignment.
            \arg \c AlignRight right alignment
        \endparblock

        \verbatim
        All commands are disabled in a verbatim block.
        参数格式:\n \param '['x']'  { parameter description }
        \endverbatim

        \par
            All commands are not disabled in a verbatim block.
            参数格式:\n \param '['x']'  { parameter description }
        \endpar

        """
        return a+b
