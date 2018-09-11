# Image Processing Libraries
Image Processing Libraries in Python


-[SciPy]
-[OpenCV](OpenCV/README.md)
-[SimpleCV](SimpleCV/README.md)
-[SimpleITK](SimpleITK/README.md)
-[pillow](pillow/README.md)
-[PIL](PIL/README.md)
-[PythonMagick](PythonMagick/README.md)
-[scikit-image](scikit-image/README.md)
-[Mahotas](Mahotas/README.md)
-[pycairo](pycairo/README.md)


|Library Name|Description|Features|Potential Disadvantages|
|-----|-----|-------|--------|
SciPy.ndimage|"scipy.ndimage packages provide various image processing functions that can be operated with arrays of any dimensionality. The packages currently include functions for linear and non-linear filtering, binary morphology, B-spline interpolation, and object measurements."||
OpenCV|OpenCV-Python is a Python wrapper for the OpenCV C++ implementation. OpenCV-Python makes use of Numpy. All the OpenCV array structures are converted to and from Numpy arrays. This also makes it easier to integrate with other libraries that use Numpy such as SciPy and Matplotlib.|"Written in C/C++ and fast
Low memory usage
Comprehensive funcionality to complete image processing
Includes statistical machine learing library"|"Complexity of use
Limited flexibility in built-in machine learning applications"
SimpleCV|"SimpleCV is an open source framework for building computer vision applications. With it, you get access to several high-powered computer vision libraries such as OpenCV � without having to first learn about bit depths, file formats, color spaces, buffer management, eigenvalues, or matrix versus bitmap storage. "|"Simple to use
Enables easy access to many OpenCV functionalities
Goof for protoytping
"|"Lack of maintenance
Poor performance compared to OpenCV
"
SimpleITK|Insight Segmentation and Registration Toolkit (ITK) provides software tools for image analysis. ITK employs leading-edge algorithms for registering and segmenting multidimensional data. SimpleITK provides a simplified interface to ITK in python and other languages.||"Limited functionality in Python, not all functions are wrapped
Centered around medical image analysis"
pillow|"Pillow is a �friendly fork� to the PIL. Development seems to have stalled on PIL, with last update made before several years, so it is been adopted as a replacement for PIL in several linux distributions. It has to be noted that Pillow and PIL cannot co-exist in the same environment and hence PIL has to be uninstalled before proceeding with Pillow."||"Native to Linux, only works on other OS's through workarounds"
PIL|"PIL (Python Imaging Library) supports opening, manipulating and saving the images in many file formats. It supports various image manipulations like filtering, enhancing, masking, handling transparency, additions and the like."||"Lack of support
Needs additional libraries to perform video processing"
PythonMagick|"PythonMagick is the Python binding of the ImageMagick which is a free software. It supports cropping, changing colors, applying various effects, adding text and geometrical figures etc. It supports reading, modifying and creating images in over 200 file formats."||
scikit-image|"scikit-image library includes algorithms for segmentation, geometric transformations, color space manipulation, analysis, filtering, morphology, feature detection in images. Its mostly written in python except for the parts written in Cython for the sake of performance. It can be interoperated with SciPy and NumPy"||Needs additional libraries to perform video processing
Mahotas|"Mahotas library provides fast computer vision algorithms like watershed, thinning, thresholding etc implemented in c++. The algorithms can be operated over numpy arrays."||
pycairo|"pycairo is a set of python bindings for the 2D graphics library cairo.They provide an object oriented interface to cairo.The Cairo library can output data to consistently to X Window system, win32 image buffers, pdf, svg files etc."||
