# ``WKInternalsNotes/_WKProcessPoolConfiguration/shouldThrowExceptionForGlobalConstantRedeclaration``

グローバル定数の再宣言時に例外を投げるかを制御する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldThrowExceptionForGlobalConstantRedeclaration WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
既定値は `true`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `shouldThrowExceptionForGlobalConstantRedeclaration` を直接操作する。

## References
- [`_WKProcessPoolConfiguration.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L130)
- [`_WKProcessPoolConfiguration.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L135)
- [`APIProcessPoolConfiguration.h#L183`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L183)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
