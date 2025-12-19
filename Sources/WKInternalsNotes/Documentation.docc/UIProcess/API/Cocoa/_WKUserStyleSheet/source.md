# ``WKInternalsNotes/_WKUserStyleSheet/source``

スタイルシートのソース文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *source;
```

## Discussion
内部の `UserStyleSheet` が保持する source を `NSString` に変換して返す。

## References
- [`_WKUserStyleSheet.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.h#L43)
- [`_WKUserStyleSheet.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
