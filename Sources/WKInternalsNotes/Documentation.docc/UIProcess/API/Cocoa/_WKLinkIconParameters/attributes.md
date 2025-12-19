# ``WKInternalsNotes/_WKLinkIconParameters/attributes``

リンクアイコンの属性辞書を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSDictionary *attributes WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`linkIcon.attributes` を `NSDictionary` に変換して保持し、そのまま返す。

## References
- [`_WKLinkIconParameters.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.h#L44)
- [`_WKLinkIconParameters.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.mm#L62)
- [`_WKLinkIconParameters.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
