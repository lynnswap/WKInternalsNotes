# ``WKInternalsNotes/_WKUserStyleSheet/baseURL``

スタイルシートの base URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSURL *baseURL;
```

## Discussion
内部の `UserStyleSheet` が保持する URL を `NSURL` に変換して返す。

## References
- [`_WKUserStyleSheet.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.h#L45)
- [`_WKUserStyleSheet.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.mm#L79)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
