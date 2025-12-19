# ``WKInternalsNotes/_WKLinkIconParameters/url``

リンクアイコンの URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSURL *url;
```

## Discussion
`linkIcon.url` を `NSURL` に変換して保持し、そのまま返す。

## References
- [`_WKLinkIconParameters.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.h#L39)
- [`_WKLinkIconParameters.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.mm#L44)
- [`_WKLinkIconParameters.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
