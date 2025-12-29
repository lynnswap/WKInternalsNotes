# ``WKInternalsNotes/_WKAppHighlight/text``

ハイライトに紐づくテキストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, strong) NSString *text;
```

## Default Value
`nil`（`initWithHighlight:text:image:` で設定される）。

## Discussion
内部で保持している `NSString` をそのまま返す。

## References
- [`_WKAppHighlight.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlight.h#L41)
- [`_WKAppHighlight.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlight.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
