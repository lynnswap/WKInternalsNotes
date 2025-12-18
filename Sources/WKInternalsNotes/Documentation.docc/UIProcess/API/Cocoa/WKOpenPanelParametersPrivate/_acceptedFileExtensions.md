# ``WKInternalsNotes/WKOpenPanelParameters/_acceptedFileExtensions``

受け付ける拡張子の一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSString *> *_acceptedFileExtensions WK_API_AVAILABLE(macos(10.13.4), ios(18.4), visionos(2.4));
```

## Default Value
`_openPanelParameters->acceptFileExtensions()` をラップした配列。

## Discussion
`acceptFileExtensions()` の結果を `wrapper(...)` で `NSArray<NSString *>` に変換して返す。

## References
- [`WKOpenPanelParametersPrivate.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKOpenPanelParametersPrivate.h#L31)
- [`WKOpenPanelParameters.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKOpenPanelParameters.mm#L59)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
