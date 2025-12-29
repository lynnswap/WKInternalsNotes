# ``WKInternalsNotes/_WKAppHighlight/highlight``

ハイライトのバイナリデータを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, strong) NSData *highlight;
```

## Default Value
`nil`（`initWithHighlight:text:image:` で設定される）。

## Discussion
内部で保持している `NSData` をそのまま返す。

## References
- [`_WKAppHighlight.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlight.h#L39)
- [`_WKAppHighlight.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlight.mm#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
