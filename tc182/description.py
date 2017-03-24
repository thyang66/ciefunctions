#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
description: Generate html description strings for the tc182 package.

Copyright (C) 2014 Ivar Farup and Jan Henrik Wold

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys


def _head():
    html_string = """
    <head>
    <link type="text/css" rel="stylesheet" href="description.css" />
    <script type="text/javascript"
    src="web/static/web/MathJax-2.4-latest/MathJax.js?config=TeX-AMS_HTML">
    </script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            displayAlign: "left",
            showProcessingMessages: false,
            messageStyle: "none",
            inlineMath:[["\\(","\\)"]],
            displayMath:[["$$","$$"]],
            "HTML-CSS": {
    """
    if sys.platform.startswith('win'):
        html_string += """
                scale: 190
        """
    elif sys.platform.startswith('linux'):
        html_string += """
                scale: 95
        """
    else:
        html_string += """
                scale: 100
        """
    html_string += """
            }
        });
    </script>
    </head>
    """
    return html_string


def _heading(heading):
    return """
    <font size="3" Color="#000099">
      <h2 class="description-heading-2">%s</h2>
    </font>
    """ % heading


def _sub_heading(sub_heading):
    return """
    <h4 class="description-heading-4">%s</h4>
    """ % sub_heading


def _parameters(data):
    return u"""
    <p>
    <b class="description-subtitle">Parameters</b>
    <table>
    <tr>
        <td>Field size</td>
        <td>: &nbsp;&nbsp; %s\u00b0 </td>
    </tr>
    <tr>
        <td>Age</td>
        <td>: &nbsp;&nbsp; %d yr</td>
    </tr>
    </table>
    </p>
    """ % (data['field_size'], data['age'])


def _parameters_31():
    return u"""
    <p>
    <b class="description-subtitle">Parameters</b>
    <table>
    <tr>
        <td>Field size</td>
        <td>: &nbsp;&nbsp; 2\u00b0 </td>
    </tr>
    </table>
    </p>
    """


def _parameters_64():
    return u"""
    <p>
    <b class="description-subtitle">Parameters</b>
    <table>
    <tr>
        <td>Field size</td>
        <td>: &nbsp;&nbsp; 10\u00b0 </td>
    </tr>
    </table>
    </p>
    """


def _functions(par1, par2, par3):
    return """
    <p>
    <b class="description-subtitle">Function symbols</b><br />
    %s &nbsp;&nbsp;&nbsp; %s &nbsp;&nbsp;&nbsp; %s
    </p>
    """ % (par1, par2, par3)


def _coordinates(par1, par2, par3):
    return """
    <p>
    <b class="description-subtitle">Coordinate symbols</b><br />
    %s &nbsp;&nbsp; %s &nbsp;&nbsp; %s
    </p>
    """ % (par1, par2, par3)


def _wavelenghts(data):
    return u"""
    <p>
    <b class="description-subtitle">Wavelenghts</b>
    <table>
    <tr>
        <td>Domain</td>
        <td>: &nbsp;&nbsp; %s&ndash;%s nm</td>
    </tr>
    <tr>
        <td>Step</td>
        <td>: &nbsp;&nbsp; %s nm</td>
    </tr>
    </table>
    </p>
    """ % (data['lambda_min'], data['lambda_max'], data['lambda_step'])


def _wavelenghts_complementary(data, options):
    if options['norm']:
        lambda_purple_min = data['lambda_purple_min_N']
        lambda_purple_max = data['lambda_purple_max_N']
    else:
        lambda_purple_min = data['lambda_purple_min']
        lambda_purple_max = data['lambda_purple_max']
    return u"""
    <p>
    <b class="description-subtitle">Wavelenghts</b>
    <table>
    <tr>
        <td>Wavelength domain of spectral stimuli</td>
        <td>: &nbsp;&nbsp; %s&ndash;%s nm</td>
    </tr>
    <tr>
        <td>Complementary-wavelength domain of purple-line stimuli</td>
        <td>: &nbsp;&nbsp; %s&ndash;%s nm</td>
    </tr>
    <tr>
        <td>Step</td>
        <td>: &nbsp;&nbsp; %s nm</td>
    </tr>
    </table>
    </p>
    """ % (data['lambda_min'], data['lambda_max'],
           lambda_purple_min, lambda_purple_max,
           data['lambda_step'])


def _wavelenghts_std():
    return u"""
    <p>
    <b class="description-subtitle">Selected wavelenghts</b>
    <table>
    <tr>
        <td>Domain</td>
        <td>: &nbsp;&nbsp; %d&ndash;%d nm</td>
    </tr>
    <tr>
        <td>Step</td>
        <td>: &nbsp;&nbsp; %d nm</td>
    </tr>
    </table>
    </p>
    """ % (360, 830, 1)


def _normalization(data):
    return u"""
    <em class="description-subtitle">Normalization:</em><br />
    Equal tristimulus values for illuminant E for
    <table>
        <tr>
            <td>Wavelength domain:</td>
            <td valign="bottom">&nbsp;%s\u2013%s&nbsp;nm</td>
        </tr>
        <tr>
            <td>Wavelength step:</td>
            <td valign="bottom">&nbsp;%s&nbsp;nm</td>
        </tr>
    </table>
    """ % (data['lambda_min'], data['lambda_max'], data['lambda_step'])


def _normalization_lms():
    return """
    <p>
    <b class="description-subtitle">Normalization</b><br />
    Function values peaking at unity at 0.1&nbsp;nm resolution<br />
    </p>
    """


def _normalization_lm(data):
    return """
    <p>
    <b class="description-subtitle">Normalization</b><br />
    The chromaticity point of illuminant E,
    \\((l_{%s,\\,%d\\mathrm{;\\,E}},\\,
    m_{%s,\\,%d\\mathrm{;\\,E}})\\), equals (1/3, 1/3).
    </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'])


def _normalization_bm(data):
    return """ <p> <b class="description-subtitle">Normalization</b><br /> The
    corresponding MacLeod&ndash;Boynton tristimulus values,
    \\(L_{\,\mathrm{MB},\,%s,\,%d}\\),
    \\(M_{\,\mathrm{MB},\,%s,\,%d}\\), and
    \\(S_{\,\mathrm{MB},\,%s,\,%d}\\), satisfy
    <br />
    &#8226;
    \\(L_{\,\mathrm{MB},\,%s,\,%d} + M_{\,\mathrm{MB},\,%s,\,%d} =
    V_{\,\mathrm{F},\,%s,\,%d}\\)
    <br />
    &#8226;
    \\(\\max\\left(
       S_{\\,\\mathrm{MB},\\,%s,\\,%d}/V_{\\,\\mathrm{F},\\,%s,\\,%d}
       \\right) =  1\\)
    <br />
    where \\(V_{\\,\\mathrm{F},\\,%s,\\,%d} = P_{\\mathrm{v}} /
      K_{\\mathrm{F,\\,m},\\,%s,\\,%d}\\), in which \\(P_{\\mathrm{v}}\\) and
    \\(K_{\\mathrm{F,\\,m},\\,%s,\\,%d}\\) are, respectively, the LM
    luminous flux and the LM maximum luminous efficacy as determined
    by the cone-fundamental-based relative spectral luminous efficiency
    function \\(V_{\\,\\mathrm{F},\\,%s,\\,%d}(\\lambda)\\).
    </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])


def _normalization_xy(data, options):
    if options['norm']:
        return """
        <p>
        <b class="description-subtitle">Normalization</b><br />
        The chromaticity point of illuminant E,
        \\((x_{\\,\\mathrm{F},\\,%s,\\,%d\\mathrm{;\\,E}},\\,
        y_{\\,\\mathrm{F},\\,%s,\\,%d\\mathrm{;\\,E}})\\), equals (1/3, 1/3)
        when calculated using a step size of %s&nbsp;nm and wavelength
        domain %s&ndash;%s&nbsp;nm.
        </p>
        """ % (data['field_size'], data['age'],
               data['field_size'], data['age'],
               data['lambda_step'],
               data['lambda_min'], data['lambda_max'])
    else:
        return """
        <p>
        <b class="description-subtitle">Normalization</b><br />
        The chromaticity point of illuminant E,
        \\((x_{\\,\\mathrm{F},\\,%s,\\,%d\\mathrm{;\\,E}},\\,
        y_{\\,\\mathrm{F},\\,%s,\\,%d\\mathrm{;\\,E}})\\), equals (1/3, 1/3)
        when calculated using a step size of 1&nbsp;nm and wavelenght
        domain 390&ndash;830&nbsp;nm.
        </p>
        """ % (data['field_size'], data['age'],
               data['field_size'], data['age'])


def _normalization_xyz(data, options):
    if options['norm']:
        return """
        <p>
        <b class="description-subtitle">Normalization</b><br />
        &#8226; Equal cone-fundamental-based tristimulus values for
        illuminant E when calculated using a step size of %s&nbsp;nm
        and wavelength domain %s&ndash;%s&nbsp;nm.<br />
        &#8226; Values of &nbsp;\\(\\bar y_{\,\mathrm{F},\,%s,\,%d}\\)
        &nbsp;peaking at unity at 0.1 nm resolution
        </p>
        """ % (data['lambda_step'],
               data['lambda_min'], data['lambda_max'],
               data['field_size'], data['age'])
    else:
        return """
        <p>
        <b class="description-subtitle">Normalization</b><br />
        &#8226; Equal cone-fundamental-based tristimulus values for
        illuminant E when calculated using a step size of 1&nbsp;nm
        and wavelenght domain 390&ndash;830&nbsp;nm.<br />
        &#8226; Values of &nbsp;\\(\\bar y_{\,\mathrm{F},\,%s,\,%d}\\)
        &nbsp;peaking at unity at 0.1 nm resolution
        </p>
        """ % (data['field_size'], data['age'])


def _normalization_31():
    return """
    <p>
    <b class="description-subtitle">Normalization</b><br />
    &#8226; Equal tristimulus values for illuminant E<br />
    &#8226; Values of &nbsp;\\(\\bar y\\)&nbsp;peaking at unity
    at 1 nm resolution
    </p>
    """


def _normalization_64():
    return """
    <p>
    <b class="description-subtitle">Normalization</b><br />
    &#8226; Equal tristimulus values for illuminant E<br />
    &#8226; Values of &nbsp;\\(\\bar y_{10}\\)&nbsp;peaking at unity
    at 1 nm resolution
    </p>
    """


def _precision_lms():
    return """
    <p>
    <b class="description-subtitle">Precision of tabulated values</b><br />
    6 significant figures<br />
    </p>
    """


def _precision_lms_base():
    return """
    <p>
    <b class="description-subtitle">Precision of tabulated values</b><br />
    9 significant figures<br />
    </p>
    """


def _precision_bm():
    return """
    <p>
    <b class="description-subtitle">Precision of tabulated values</b><br />
    6 decimal places<br />
    </p>
    """


def _precision_lm():
    return """
    <p>
    <b class="description-subtitle">Precision of tabulated values</b><br />
    6 decimal places<br />
    </p>
    """


def _precision_xyz():
    return """
    <p>
    <b class="description-subtitle">Precision of tabulated values</b><br />
    7 significant figures<br />
    </p>
    """


def _precision_xy():
    return """
    <p>
    <b class="description-subtitle">Precision of tabulated values</b><br />
    5 decimal places<br />
    </p>
    """


def _lms_to_xyz(data, options, purple=False):
    if options['norm']:
        trans_mat = data['trans_mat_N']
    else:
        trans_mat = data['trans_mat']
    html_string = """
        <b class="description-subtitle">Transformation equation</b><br />
    """
    if purple:
        html_string += """
        The corresponding transformation from CIE LMS cone
        fundamentals to CIE XYZ cone-fundamental-based spectral
        tristimulus values is:<br />
        """
    html_string += """
        $$
        \\begin{pmatrix}
        \\bar x_{\,\mathrm{F},\,%s,\,%d}(\\lambda) \\\\
        \\bar y_{\,\mathrm{F},\,%s,\,%d}(\\lambda) \\\\
        \\bar z_{\,\mathrm{F},\,%s,\,%d}(\\lambda)
        \\end{pmatrix}
        = \\begin{pmatrix}
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    for i in range(3):
        for j in range(3):
            if trans_mat[i][j] == 0:
                html_string = html_string + """
                0
                """
            else:
                html_string = html_string + '%0.8f\n' % trans_mat[i][j]
            html_string += '&'
        html_string = html_string + '\\\\'
    html_string += """
        \\end{pmatrix}
        \\begin{pmatrix}
        \\bar l_{%s,\,%d}(\\lambda) \\\\
        \\bar m_{\,%s,\,%d}(\\lambda) \\\\
        \\bar s_{%s,\,%d}(\\lambda)
        \\end{pmatrix}
        $$
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    html_string += """
        <p>
        with the cone fundamentals \\( \,\\bar l_{%s,\,%d}(\\lambda),\;
        \\bar m_{\,%s,\,%d}(\\lambda),\; \\bar s_{%s,\,%d}(\\lambda)\\)
        &nbsp;given to the precision of 9 significant figures
        </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    return html_string


def _lms_to_xyz_purple(data, options):
    return _lms_to_xyz(data, options, True)


def _lms_to_bm(data, options):
    if options['norm']:
        trans_mat = data['trans_mat_N']
    else:
        trans_mat = data['trans_mat']
    html_string = """
        <p>
        <b class="description-subtitle">Transformation equations</b><br />
        $$
        \\begin{aligned}
        l_{\,\mathrm{MB},\,%s,\,%d}(\\lambda)\\; &= \\frac{%.8f\\,
        \\bar l_{%s,\,%d}(\\lambda)}{%.8f\\, \\bar
        l_{%s,\,%d}(\\lambda) + %.8f\\, \\bar m_{\,%s,\,%d}(\\lambda)}
        \\\\ m_{\,\mathrm{MB},\,%s,\,%d}(\\lambda)\\; &=
        \\frac{%.8f\\, \\bar m_{\,%s,\,%d}(\\lambda)}{%.8f\\, \\bar
        l_{%s,\,%d}(\\lambda) + %.8f\\, \\bar m_{\,%s,\,%d}(\\lambda)}
        \\\\ s_{\,\mathrm{MB},\,%s,\,%d}(\\lambda)\\; &=
        \\frac{%.8f\\, \\bar s_{%s,\,%d}(\\lambda)}{%.8f\\, \\bar
        l_{%s,\,%d}(\\lambda) + %.8f\\, \\bar m_{\,%s,\,%d}(\\lambda)}
        \\\\
        \\end{aligned}
        $$
        </p>
    """ % (data['field_size'], data['age'],
           trans_mat[1, 0], data['field_size'], data['age'],
           trans_mat[1, 0], data['field_size'], data['age'],
           trans_mat[1, 1], data['field_size'], data['age'],
           data['field_size'], data['age'],
           trans_mat[1, 1], data['field_size'], data['age'],
           trans_mat[1, 0], data['field_size'], data['age'],
           trans_mat[1, 1], data['field_size'], data['age'],
           data['field_size'], data['age'],
           1./data['bm_s_max'], data['field_size'], data['age'],
           trans_mat[1, 0], data['field_size'], data['age'],
           trans_mat[1, 1], data['field_size'], data['age'])
    html_string += """
        <p>
        with the cone fundamentals \\( \,\\bar
        l_{%s,\,%d}(\\lambda),\; \\bar m_{\,%s,\,%d}(\\lambda),\;
        \\bar s_{%s,\,%d}(\\lambda)\\) &nbsp;given to the precision of
        9 significant figures
        </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    return html_string


def _lms_to_lm(data):
    html_string = """
    <p>
    <b class="description-subtitle">Transformation equations</b><br />
    $$
    \\begin{aligned}
    l_{\,%s,\,%d}(\\lambda)\\; &=
    \\frac{%.8f\\, \\bar l_{%s,\,%d}(\\lambda)}{%.8f\\, \\bar l_{%s,\,%d}
    (\\lambda) + %.8f\\, \\bar m_{\,%s,\,%d}(\\lambda) + %.8f\\,
    \\bar s_{%s,\,%d}(\\lambda)} \\\\
    m_{\,%s,\,%d}(\\lambda)\\; &=
    \\frac{%.8f\\, \\bar m_{\,%s,\,%d}(\\lambda)}{%.8f\\, \\bar l_{%s,\,%d}
    (\\lambda) + %.8f\\, \\bar m_{\,%s,\,%d}(\\lambda) + %.8f\\,
    \\bar s_{%s,\,%d}(\\lambda)} \\\\
    s_{\,%s,\,%d}(\\lambda)\\; &=
    \\frac{%.8f\\, \\bar s_{%s,\,%d}(\\lambda)}{%.8f\\, \\bar l_{%s,\,%d}
    (\\lambda) + %.8f\\, \\bar m_{\,%s,\,%d}(\\lambda) + %.8f\\,
    \\bar s_{%s,\,%d}(\\lambda)} \\\\
    \\end{aligned}
    $$
    </p>
    """ % (data['field_size'], data['age'],
           data['lms_N_inv'][0], data['field_size'], data['age'],
           data['lms_N_inv'][0], data['field_size'], data['age'],
           data['lms_N_inv'][1], data['field_size'], data['age'],
           data['lms_N_inv'][2], data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['lms_N_inv'][1], data['field_size'], data['age'],
           data['lms_N_inv'][0], data['field_size'], data['age'],
           data['lms_N_inv'][1], data['field_size'], data['age'],
           data['lms_N_inv'][2], data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['lms_N_inv'][2], data['field_size'], data['age'],
           data['lms_N_inv'][0], data['field_size'], data['age'],
           data['lms_N_inv'][1], data['field_size'], data['age'],
           data['lms_N_inv'][2], data['field_size'], data['age'])
    html_string += """
        <p>
        with the cone fundamentals \\( \,\\bar
        l_{%s,\,%d}(\\lambda),\; \\bar m_{\,%s,\,%d}(\\lambda),\;
        \\bar s_{%s,\,%d}(\\lambda)\\) &nbsp;given to the precision of
        9 significant figures
        </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    return html_string


def _xyz_to_xy(data):
    html_string = """
    <b class="description-subtitle">Transformation equations</b><br />
    $$
    \\begin{aligned}
    x_{\,\mathrm{F},\,%s,\,%d}(\\lambda)\\; &=
    \\frac{\\bar x_{\,\mathrm{F},\,%s,\,%d}(\\lambda)}
    {\\bar x_{\,\mathrm{F},\,%s,\,%d}(\\lambda) +
    \\bar y_{\,\mathrm{F},\,%s,\,%d}(\\lambda) +
    \\bar z_{\,\mathrm{F},\,%s,\,%d}(\\lambda)} \\\\
    y_{\,\mathrm{F},\,%s,\,%d}(\\lambda)\\; &=
    \\frac{\\bar y_{\,\mathrm{F},\,%s,\,%d}(\\lambda)}
    {\\bar x_{\,\mathrm{F},\,%s,\,%d}(\\lambda) +
    \\bar y_{\,\mathrm{F},\,%s,\,%d}(\\lambda) +
    \\bar z_{\,\mathrm{F},\,%s,\,%d}(\\lambda)} \\\\
    z_{\,\mathrm{F},\,%s,\,%d}(\\lambda)\\; &=
    \\frac{\\bar z_{\,\mathrm{F},\,%s,\,%d}(\\lambda)}
    {\\bar x_{\,\mathrm{F},\,%s,\,%d}(\\lambda) +
    \\bar y_{\,\mathrm{F},\,%s,\,%d}(\\lambda) +
    \\bar z_{\,\mathrm{F},\,%s,\,%d}(\\lambda)} \\\\
    \\end{aligned}
    $$
    </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    html_string += """
        <p>
        with the cone-fundamental-based spectral tristimulus values
        \\( \,\\bar x_{\,\mathrm{F},\,%s,\,%d}(\\lambda)\\), \\(
        \,\\bar y_{\,\mathrm{F},\,%s,\,%d}(\\lambda)\\), \\( \,\\bar
        z_{\,\mathrm{F},\,%s,\,%d}(\\lambda)\\) &nbsp;given to the
        precision of 7 significant figures
        </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    return html_string


def _xyz_to_xy_complementary(data):
    html_string = """
    <b class="description-subtitle">Transformation equations</b><br />
    $$
    \\begin{aligned}
    x_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})\\; &=
    \\frac{\\bar x_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})}
    {\\bar x_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}}) +
    \\bar y_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}}) +
    \\bar z_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})} \\\\
    y_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})\\; &=
    \\frac{\\bar y_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})}
    {\\bar x_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}}) +
    \\bar y_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}}) +
    \\bar z_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})} \\\\
    z_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})\\; &=
    \\frac{\\bar z_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})}
    {\\bar x_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}}) +
    \\bar y_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}}) +
    \\bar z_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})} \\\\
    \\end{aligned}
    $$
    </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    html_string += """
        <p>
        with the cone-fundamental-based spectral tristimulus values for purple-line stimuli,
        \\( \,\\bar x_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})\\), \\(
        \,\\bar y_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})\\), \\( \,\\bar
        z_{\,\mathrm{Fp},\,%s,\,%d}(\\lambda_{\\,\\mathrm{c}})\\), &nbsp;given to the
        precision of 7 significant figures
        </p>
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['field_size'], data['age'])
    return html_string


def _xyz_to_xy_31():
    return """
    <b class="description-subtitle">Transformation equations</b><br />
    $$
    \\begin{aligned}
    x(\\lambda)\\; &= \\frac{\\bar x(\\lambda)}{\\bar x(\\lambda) +
    \\bar y(\\lambda) + \\bar z(\\lambda)} \\\\
    y(\\lambda)\\; &= \\frac{\\bar y(\\lambda)}{\\bar x(\\lambda) +
    \\bar y(\\lambda) + \\bar z(\\lambda)} \\\\
    z(\\lambda)\\; &= \\frac{\\bar z(\\lambda)}{\\bar x(\\lambda) +
    \\bar y(\\lambda) + \\bar z(\\lambda)} \\\\
    \\end{aligned}
    $$
    </p>
    """


def _xyz_to_xy_64():
    return """
    <b class="description-subtitle">Transformation equations</b><br />
    $$
    \\begin{aligned}
    x_{10}(\\lambda)\\; &=
    \\frac{\\bar x_{10}(\\lambda)}{\\bar x_{10}(\\lambda) +
    \\bar y_{10}(\\lambda) + \\bar z_{10}(\\lambda)} \\\\
    y_{\,10}(\\lambda)\\; &=
    \\frac{\\bar y_{10}(\\lambda)}{\\bar x_{10}(\\lambda) +
    \\bar y_{10}(\\lambda) +
    \\bar z_{10}(\\lambda)} \\\\
    z_{\,10}(\\lambda)\\; &=
    \\frac{\\bar z_{10}(\\lambda)}{\\bar x_{10}(\\lambda) +
    \\bar y_{10}(\\lambda) +
    \\bar z_{10}(\\lambda)} \\\\
    \\end{aligned}
    $$
    </p>
    """


def _illuminant_E_cc(data, options):
    if options['norm']:
        xy_white = data['xy_white_N']
    else:
        xy_white = data['xy_white']
    return """
    <b class="description-subtitle">Chromaticity point of illuminant E</b>
    <br />
    \\( (x_{\,\mathrm{F},\,%s,\,%d;\,\\mathrm{E}},\\,
    \\,y_{\,\mathrm{F},\,%s,\,%d;\,\\mathrm{E}}) =
    (%.5f, %.5f) \\)<br /><br />
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           xy_white[0], xy_white[1])


def _illuminant_E_cc_31():
    return """
    <p>
    <b class="description-subtitle">Chromaticity point of illuminant E</b>
    <br />
    \\((x_{\mathrm{E}},\,y_{\,\mathrm{E}}) = (0.33331,0.33329) \\)
    </p>
    """


def _illuminant_E_cc_64():
    return """
    <p>
    <b class="description-subtitle">Chromaticity point of illuminant E</b>
    <br />
    \\((x_{10;\,\mathrm{E}},\,y_{\,10;\,\mathrm{E}}) = (0.33330, 0.33333) \\)
    </p>
    """


def _illuminant_E_lm(data):
    return """
    <b class="description-subtitle">Chromaticity point of illuminant E</b>
    <br />
    \\( (l_{\,%s,\,%d;\,\mathrm{E}},\,m_{\,%s,\,%d;\,\mathrm{E}}) =
    (%.6f, %.6f)\\) <br /><br />
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['lm_white'][0], data['lm_white'][1])


def _illuminant_E_bm(data):
    return """
    <b class="description-subtitle">Chromaticity point of illuminant E</b>
    <br />
    \\( (l_{\,\mathrm{MB},\,%s,\,%d;\,\mathrm{E}},
    \,s_{\,\mathrm{MB},\,%s,\,%d;\,\mathrm{E}}) =
    (%.6f, %.6f)\\) <br /><br />
    """ % (data['field_size'], data['age'],
           data['field_size'], data['age'],
           data['bm_white'][0], data['bm_white'][2])


def _purple_cc(data, options):
    if options['norm']:
        purple_line_cc = data['purple_line_cc_N']
    else:
        purple_line_cc = data['purple_line_cc']
    return """
    <b class="description-subtitle">Tangent points of the purple line</b><br />
    $$
    \\begin{align}
    (x_{\,\mathrm{F},\,%s,\,%d}(%.1f\,\mathrm{nm}),
    \,y_{\,\mathrm{F},\,%s,\,%d}(%.1f\,\mathrm{nm})) &= (%.5f, %.5f) \\\\
    (x_{\,\mathrm{F},\,%s,\,%d}(%.1f\,\mathrm{nm}),
    \,y_{\,\mathrm{F},\,%s,\,%d}(%.1f\,\mathrm{nm})) &= (%.5f, %.5f) \\\\
    \\end{align}
    $$
    """ % (data['field_size'], data['age'], purple_line_cc[0, 0],
           data['field_size'], data['age'], purple_line_cc[0, 0],
           purple_line_cc[0, 1], purple_line_cc[0, 2],
           data['field_size'], data['age'], purple_line_cc[1, 0],
           data['field_size'], data['age'], purple_line_cc[1, 0],
           purple_line_cc[1, 1], purple_line_cc[1, 2])


def _purple_31(data):
    return """
    <b class="description-subtitle">Tangent points of the purple line</b><br />
    $$
    \\begin{align}
    (x(%.1f\,\mathrm{nm}),\,y(%.1f\,\mathrm{nm})) &= (%.5f, %.5f) \\\\
    (x(%.1f\,\mathrm{nm}),\,y(%.1f\,\mathrm{nm})) &= (%.5f, %.5f) \\\\
    \\end{align}
    $$
    """ % (data['purple_line_cc31'][0, 0],
           data['purple_line_cc31'][0, 0],
           data['purple_line_cc31'][0, 1], data['purple_line_cc31'][0, 2],
           data['purple_line_cc31'][1, 0],
           data['purple_line_cc31'][1, 0],
           data['purple_line_cc31'][1, 1], data['purple_line_cc31'][1, 2])


def _purple_64(data):
    return """
    <b class="description-subtitle">Tangent points of the purple line</b><br />
    $$
    \\begin{align}
    (x_{10}(%.1f\,\mathrm{nm}),\,y_{\,10}(%.1f\,\mathrm{nm})) &=
    (%.5f, %.5f) \\\\
    (x_{10}(%.1f\,\mathrm{nm}),\,y_{\,10}(%.1f\,\mathrm{nm})) &=
    (%.5f, %.5f) \\\\
    \\end{align}
    $$
    """ % (data['purple_line_cc64'][0, 0],
           data['purple_line_cc64'][0, 0],
           data['purple_line_cc64'][0, 1], data['purple_line_cc64'][0, 2],
           data['purple_line_cc64'][1, 0],
           data['purple_line_cc64'][1, 0],
           data['purple_line_cc64'][1, 1], data['purple_line_cc64'][1, 2])


def _purple_lm(data):
    return """
    <b class="description-subtitle">Tangent points of the purple line</b><br />
    $$
    \\begin{align}
    (l_{\,%s,\,%d}(%.1f\,\mathrm{nm}),\,s_{\,%s,\,%d}(%.1f\,\mathrm{nm})) &=
    (%.6f, %.6f) \\\\
    (l_{\,%s,\,%d}(%.1f\,\mathrm{nm}),\,s_{\,%s,\,%d}(%.1f\,\mathrm{nm})) &=
    (%.6f, %.6f) \\\\
    \\end{align}
    $$
    """ % (data['field_size'], data['age'], data['purple_line_lm'][0, 0],
           data['field_size'], data['age'], data['purple_line_lm'][0, 0],
           data['purple_line_lm'][0, 1], data['purple_line_lm'][0, 2],
           data['field_size'], data['age'], data['purple_line_lm'][1, 0],
           data['field_size'], data['age'], data['purple_line_lm'][1, 0],
           data['purple_line_lm'][1, 1], data['purple_line_lm'][1, 2])


def _purple_bm(data):
    return """
    <b class="description-subtitle">Tangent points of the purple line</b><br />
    $$
    \\begin{align}
    (l_{\,\mathrm{MB},\,%s,\,%d}(%.1f\,\mathrm{nm}),
    \,s_{\,\mathrm{MB},\,%s,\,%d}(%.1f\,\mathrm{nm})) &= (%.6f, %.6f) \\\\
    (l_{\,\mathrm{MB},\,%s,\,%d}(%.1f\,\mathrm{nm}),
    \,s_{\,\mathrm{MB},\,%s,\,%d}(%.1f\,\mathrm{nm})) &= (%.6f, %.6f) \\\\
    \\end{align}
    $$
    """ % (data['field_size'], data['age'], data['purple_line_bm'][0, 0],
           data['field_size'], data['age'], data['purple_line_bm'][0, 0],
           data['purple_line_bm'][0, 1], data['purple_line_bm'][0, 2],
           data['field_size'], data['age'], data['purple_line_bm'][1, 0],
           data['field_size'], data['age'], data['purple_line_bm'][1, 0],
           data['purple_line_bm'][1, 1], data['purple_line_bm'][1, 2])


def xyz(data, heading, options, include_head=False):
    """
    Generate html page with information about the XYZ system.

    Parameters
    ----------
    data : dict
        Computed CIE functions as returned from the tc182 module.
    heading : string
        The heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters(data) +
                    _functions('\\(\\bar x_{\,\mathrm{F},\,%s,\,%d}\\)' %
                               (data['field_size'], data['age']),
                               '\\(\\bar y_{\,\mathrm{F},\,%s,\,%d}\\)' %
                               (data['field_size'], data['age']),
                               '\\(\\bar z_{\,\mathrm{F},\,%s,\,%d}\\)' %
                               (data['field_size'], data['age'])) +
                    _wavelenghts(data) +
                    _normalization_xyz(data, options) +
                    _lms_to_xyz(data, options) +
                    _precision_xyz())
    return html_string


def purple(data, heading, options, include_head=False):
    """
    Generate html page with information about the purple XYZ.

    Parameters
    ----------
    data : dict
        Computed CIE functions as returned from the tc182 module.
    heading : string
        The heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters(data) +
                    _functions('\\(\\bar x_{\,\mathrm{Fp},\,%s,\,%d}\\)' %
                               (data['field_size'], data['age']),
                               '\\(\\bar y_{\,\mathrm{Fp},\,%s,\,%d}\\)' %
                               (data['field_size'], data['age']),
                               '\\(\\bar z_{\,\mathrm{Fp},\,%s,\,%d}\\)' %
                               (data['field_size'], data['age'])) +
                    _wavelenghts_complementary(data, options) +
                    _normalization_xyz(data, options) +
                    _lms_to_xyz_purple(data, options) +
                    _precision_xyz())
    return html_string


def purple_cc(data, heading, options, include_head=False):
    """
    Generate html page with information about the xy system (purple stimuli).

    Parameters
    ----------
    data : dict
        Computed CIE functions as returned from the tc182 module.
    heading : string
        The heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters(data) +
                    _coordinates('\\(x_{\,\mathrm{Fp},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age']),
                                 '\\(y_{\,\mathrm{Fp},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age']),
                                 '\\(z_{\,\mathrm{Fp},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age'])) +
                    _wavelenghts_complementary(data, options) +
                    _normalization_xy(data, options) +
                    _xyz_to_xy_complementary(data) +
                    _precision_xy() +
                    _illuminant_E_cc(data, options) +
                    _purple_cc(data, options))
    return html_string


def xy(data, heading, options, include_head=False):
    """
    Generate html page with information about the xy system.

    Parameters
    ----------
    data : dict
        Computed CIE functions as returned from the tc182 module.
    heading : string
        The heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters(data) +
                    _coordinates('\\(x_{\,\mathrm{F},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age']),
                                 '\\(y_{\,\mathrm{F},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age']),
                                 '\\(z_{\,\mathrm{F},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age'])) +
                    _wavelenghts(data) +
                    _normalization_xy(data, options) +
                    _xyz_to_xy(data) +
                    _precision_xy() +
                    _illuminant_E_cc(data, options) +
                    _purple_cc(data, options))
    return html_string


def lms(data, heading, options, include_head=False):
    """
    Generate html page with information about the LMS system.

    Parameters
    ----------
    data : dict
        Computed CIE functions as returned from the tc182 module.
    heading : string
        The heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters(data) +
                    _functions('\\(\\bar l_{%s,\,%d}\\)' %
                               (data['field_size'], data['age']),
                               '\\(\\bar m_{\,%s,\,%d}\\)' %
                               (data['field_size'], data['age']),
                               '\\(\\bar s_{%s,\,%d}\\)' %
                               (data['field_size'], data['age'])) +
                    _wavelenghts(data) +
                    _normalization_lms() +
                    _precision_lms())
    return html_string


def lms_base(data, heading, options, include_head=False):
    """
    Generate html page with information about the LMS system.

    Parameters
    ----------
    data : dict
        Computed CIE functions as returned from the tc182 module.
    heading : string
        The heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters(data) +
                    _functions('\\(\\bar l_{%s,\,%d}\\)' %
                               (data['field_size'], data['age']),
                               '\\(\\bar m_{\,%s,\,%d}\\)' %
                               (data['field_size'], data['age']),
                               '\\(\\bar s_{%s,\,%d}\\)' %
                               (data['field_size'], data['age'])) +
                    _wavelenghts(data) +
                    _normalization_lms() +
                    _precision_lms_base())
    return html_string


def bm(data, heading, options, include_head=False):
    """
    Generate html page with information about the BM system.

    Parameters
    ----------
    data : dict
        Computed CIE functions as returned from the tc182 module.
    heading : string
        The heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters(data) +
                    _coordinates('\\(l_{\,\mathrm{MB},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age']),
                                 '\\(m_{\,\mathrm{MB},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age']),
                                 '\\(s_{\,\mathrm{MB},\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age'])) +
                    _wavelenghts(data) +
                    _normalization_bm(data) +
                    _lms_to_bm(data, options) +
                    _precision_bm() +
                    _illuminant_E_bm(data) +
                    _purple_bm(data))
    return html_string


def lm(data, heading, options, include_head=False):
    """
    Generate html page with information about the lm system.

    Parameters
    ----------
    data : dict
        Computed CIE functions as returned from the tc182 module.
    heading : string
        The heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters(data) +
                    _coordinates('\\(l_{\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age']),
                                 '\\(m_{\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age']),
                                 '\\(s_{\,%s,\,%d}\\)' %
                                 (data['field_size'], data['age'])) +
                    _wavelenghts(data) +
                    _normalization_lm(data) +
                    _lms_to_lm(data) +
                    _precision_lm() +
                    _illuminant_E_lm(data) +
                    _purple_lm(data))
    return html_string


def xyz31(data, heading, options, include_head=False):
    """
    Generate html page with information about the standard

    Parameters
    ----------
    heading : string
        The heading of the page.
    sub_heading : string
        The sub-heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters_31() +
                    _functions('\\(\\bar x\\)',
                               '\\(\\bar y\\)',
                               '\\(\\bar z\\)') +
                    _wavelenghts_std() +
                    _normalization_31() +
                    _precision_xyz())
    return html_string


def xyz64(data, heading, options, include_head=False):

    """
    Generate html page with information about the standard

    Parameters
    ----------
    heading : string
        The heading of the page.
    sub_heading : string
        The sub-heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters_64() +
                    _functions('\\(\\bar x_{10}\\)',
                               '\\(\\bar y_{10}\\)',
                               '\\(\\bar z_{10}\\)') +
                    _wavelenghts_std() +
                    _normalization_64() +
                    _precision_xyz())
    return html_string


def xy31(data, heading, options, include_head=False):
    """
    Generate html page with information about the standard

    Parameters
    ----------
    heading : string
        The heading of the page.
    sub_heading : string
        The sub-heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters_31() +
                    _coordinates('\\(x\\)', '\\(y\\)', '\\(z\\)') +
                    _wavelenghts_std() +
                    _xyz_to_xy_31() +
                    _precision_xy() +
                    _illuminant_E_cc_31() +
                    _purple_31(data))
    return html_string


def xy64(data, heading, options, include_head=False):
    """
    Generate html page with information about the standard

    Parameters
    ----------
    heading : string
        The heading of the page.
    sub_heading : string
        The sub-heading of the page.
    include_head : bool
        Indlue html head with css (for matrix etc.)

    Returns
    -------
    html_string : string
        The generated page.
    """
    html_string = ""
    if include_head:
        html_string += _head()
    html_string += (_heading(heading) +
                    _parameters_64() +
                    _coordinates('\\(x_{10}\\)',
                                 '\\(y_{\,10}\\)',
                                 '\\(z_{\,10}\\)') +
                    _wavelenghts_std() +
                    _xyz_to_xy_64() +
                    _precision_xy() +
                    _illuminant_E_cc_64() +
                    _purple_64(data))
    return html_string
