// SPDX-License-Identifier: BSD-3-Clause
// Copyright (c) Contributors to the OpenEXR Project.

// This file is auto-generated by the configure step

#ifndef INCLUDED_OPENEXR_CONFIG_H
#define INCLUDED_OPENEXR_CONFIG_H 1

#pragma once

//
// The OpenEXR release version is defined officially in
// src/lib/OpenEXRCore/openexr_version.h, but CMake doesn't readily allow
// that to be included here, so duplicate the settings for
// backwards-compatibility with applications that may expect to get the
// defines from this include.
//

#ifndef INCLUDED_OPENEXR_VERSION_H
#define OPENEXR_VERSION_MAJOR 3
#define OPENEXR_VERSION_MINOR 2
#define OPENEXR_VERSION_PATCH 2
#endif

//
// Options / configuration based on O.S. / compiler
/////////////////////

// automated formatting does not handle the cmake tags well
// clang-format off

//
// Define and set to 1 if the target system has support for large
// stack sizes.
//
/* #undef OPENEXR_HAVE_LARGE_STACK */

//////////////////////
//
// C++ namespace configuration / options

//
// Current internal library namespace name
//
#define OPENEXR_IMF_INTERNAL_NAMESPACE_CUSTOM 0
#define OPENEXR_IMF_INTERNAL_NAMESPACE Imf_3_2

//
// Current public user namespace name
//

#define OPENEXR_IMF_NAMESPACE_CUSTOM 0
#define OPENEXR_IMF_NAMESPACE Imf

//
// Version string for runtime access
//

#define OPENEXR_VERSION_STRING "3.2.2"
#define OPENEXR_PACKAGE_STRING "OpenEXR 3.2.2"

#define OPENEXR_VERSION_RELEASE_TYPE ""
// Deprecated, for back compatibility:
#define OPENEXR_VERSION_EXTRA ""

#define OPENEXR_LIB_VERSION_STRING "31.3.2.2"

// clang-format on

// Version as a single hex number, e.g. 0x01000300 == 1.0.3
#define OPENEXR_VERSION_HEX                                           \
    (((OPENEXR_VERSION_MAJOR) << 24) |                                \
     ((OPENEXR_VERSION_MINOR) << 16) |                                \
     ((OPENEXR_VERSION_PATCH) << 8))

// On modern versions of gcc & clang, __has_attribute can test support for
// __attribute__((attr)).  Make sure it's safe for other compilers.
#ifndef __has_attribute
#    define __has_attribute(x) 0
#endif

// Whether the user configured the library to have symbol visibility
// tagged
#define OPENEXR_ENABLE_API_VISIBILITY

/// \defgroup ExportMacros Macros to manage symbol visibility
///
/// See website/SymbolVisibility.rst for more discussion about the
/// motivation for these macros
///
/// If we are compiling a DLL for Windows, there needs to be custom
/// rules for each library such that the macro swaps between doing a
/// dllexport and a dllimport, so the defines here are less
/// useful. Further, MSVC does not have this concept at all currently,
/// so is elided.
///
/// The top level macros which start with OPENEXR can act as simple
/// ways to combine the logic however for non-DLL or non-windows
/// platforms, but until the current patterns change, one should check
/// the specific library export.h (i.e. @sa IexExport.h,
/// @sa IlmThreadExport.h, @sa ImfExport.h, @sa ImfUtilExport.h )
///
/// These per-library exports define a subset which are used by that
/// library.
///
/// Iex is simple and does not need to do more than expose class types
/// and functions, and does not have any private members to hide, so
/// only provides a couple of the possible macros.
///
/// Similarly, IlmThread is also reasonably simple.
///
/// OpenEXR and OpenEXRUtil have much more logic and have to deal with
/// templates and template instantiation, and so define more of the
/// macros.
///
/// @{

#if defined(OPENEXR_ENABLE_API_VISIBILITY) &&                                  \
    !(defined(OPENEXR_DLL) || defined(_MSC_VER))
#    define OPENEXR_PUBLIC_SYMBOL_ATTRIBUTE                                    \
        __attribute__ ((__visibility__ ("default")))
#    define OPENEXR_PRIVATE_SYMBOL_ATTRIBUTE                                   \
        __attribute__ ((__visibility__ ("hidden")))
// clang differs from gcc and has type visibility which is needed
// for enums and templates, and isn't well documented, but causes
// the vtable and typeinfo to be made visible, but not necessarily
// all the members
#    if __has_attribute(__type_visibility__)
#        define OPENEXR_PUBLIC_TYPE_VISIBILITY_ATTRIBUTE                       \
            __attribute__ ((__type_visibility__ ("default")))
#    endif

// these are always the same, at least in current compilers
#    define OPENEXR_EXPORT OPENEXR_PUBLIC_SYMBOL_ATTRIBUTE
#    define OPENEXR_HIDDEN OPENEXR_PRIVATE_SYMBOL_ATTRIBUTE
// currently define this as the same between compilers to export
// things like default copy ctors etc, and do not use the type
// visibility which only exports the typeinfo / vtable
#    define OPENEXR_EXPORT_TYPE OPENEXR_EXPORT
#    define OPENEXR_EXPORT_EXTERN_TEMPLATE OPENEXR_EXPORT

#    ifdef OPENEXR_PUBLIC_TYPE_VISIBILITY_ATTRIBUTE
#        define OPENEXR_EXPORT_ENUM OPENEXR_PUBLIC_TYPE_VISIBILITY_ATTRIBUTE
#        define OPENEXR_EXPORT_TEMPLATE_TYPE                                   \
            OPENEXR_PUBLIC_TYPE_VISIBILITY_ATTRIBUTE
// clang (well, type_visibility) seems empirically need the
// default/public symbol tag when specifying explicit template
// instantiations, where gcc (no type_visibility) complains if
// you set that
#        define OPENEXR_EXPORT_TEMPLATE_INSTANCE OPENEXR_EXPORT
#    else
#        define OPENEXR_EXPORT_ENUM
#        define OPENEXR_EXPORT_TEMPLATE_TYPE OPENEXR_EXPORT
#        define OPENEXR_EXPORT_TEMPLATE_INSTANCE
#    endif

#else // msvc or api visibility disabled, just clear all this out (DLLs will define a set anyway)

#    define OPENEXR_EXPORT
#    define OPENEXR_HIDDEN
#    define OPENEXR_EXPORT_TYPE
#    define OPENEXR_EXPORT_EXTERN_TEMPLATE
#    define OPENEXR_EXPORT_ENUM
#    define OPENEXR_EXPORT_TEMPLATE_TYPE
#    define OPENEXR_EXPORT_TYPE
#    define OPENEXR_EXPORT_TEMPLATE_INSTANCE

#endif

#if defined(__cplusplus) && (__cplusplus >= 201402L)
#    define OPENEXR_DEPRECATED(msg) [[deprecated (msg)]]
#endif

#ifndef OPENEXR_DEPRECATED
#    ifdef _MSC_VER
#        define OPENEXR_DEPRECATED(msg) __declspec(deprecated (msg))
#    else
#        define OPENEXR_DEPRECATED(msg) __attribute__ ((deprecated (msg)))
#    endif
#endif

#endif // INCLUDED_OPENEXR_CONFIG_H
