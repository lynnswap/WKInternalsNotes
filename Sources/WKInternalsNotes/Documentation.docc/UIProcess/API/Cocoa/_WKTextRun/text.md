# ``WKInternalsNotes/_WKTextRun/text``

内部の `API::TextRun` が保持する文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *text;
```

## Default Value
`API::TextRun` の文字列に依存。

## Discussion
`_textRun->string()` を `NSString` に変換して返す。

## References
- [`_WKTextRun.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextRun.h#L35)
- [`_WKTextRun.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextRun.mm#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
