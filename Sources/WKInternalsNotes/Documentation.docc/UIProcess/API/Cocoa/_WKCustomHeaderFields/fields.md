# ``WKInternalsNotes/_WKCustomHeaderFields/fields``

追加するカスタムヘッダの辞書を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSDictionary<NSString *, NSString *> *fields;
```

## Discussion
内部の `CustomHeaderFields` から辞書を生成して返す。setter では `x-` で始まるヘッダ名のみを抽出して保持する。

## References
- [`_WKCustomHeaderFields.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKCustomHeaderFields.h#L33)
- [`_WKCustomHeaderFields.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKCustomHeaderFields.mm#L53)
- [`_WKCustomHeaderFields.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKCustomHeaderFields.mm#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
