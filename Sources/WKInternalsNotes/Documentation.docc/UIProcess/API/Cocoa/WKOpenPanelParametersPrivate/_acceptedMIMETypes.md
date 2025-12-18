# ``WKInternalsNotes/WKOpenPanelParameters/_acceptedMIMETypes``

受け付ける MIME type の一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSString *> *_acceptedMIMETypes WK_API_AVAILABLE(macos(10.13.4), ios(18.4), visionos(2.4));
```

## Default Value
`_openPanelParameters->acceptMIMETypes()` をラップした配列。

## Discussion
`acceptMIMETypes()` の結果を `wrapper(...)` で `NSArray<NSString *>` に変換して返す。

## References
- [`WKOpenPanelParametersPrivate.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKOpenPanelParametersPrivate.h#L30)
- [`WKOpenPanelParameters.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKOpenPanelParameters.mm#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
