# ``WKInternalsNotes/WKOpenPanelParameters/_allowedFileExtensions``

許可される拡張子の一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSString *> *_allowedFileExtensions WK_API_AVAILABLE(macos(11.0), ios(18.4), visionos(2.4));
```

## Default Value
`_openPanelParameters->allowedFileExtensions()` をラップした配列。

## Discussion
`allowedFileExtensions()` の結果を `wrapper(...)` で `NSArray<NSString *>` に変換して返す。

## References
- [`WKOpenPanelParametersPrivate.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKOpenPanelParametersPrivate.h#L32)
- [`WKOpenPanelParameters.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKOpenPanelParameters.mm#L64)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
