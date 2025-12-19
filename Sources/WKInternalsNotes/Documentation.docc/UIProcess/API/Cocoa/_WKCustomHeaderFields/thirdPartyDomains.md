# ``WKInternalsNotes/_WKCustomHeaderFields/thirdPartyDomains``

カスタムヘッダの適用対象となるサードパーティドメインを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<NSString *> *thirdPartyDomains;
```

## Discussion
内部の `CustomHeaderFields` に対してドメイン配列を読み書きする。

## References
- [`_WKCustomHeaderFields.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKCustomHeaderFields.h#L34)
- [`_WKCustomHeaderFields.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKCustomHeaderFields.mm#L73)
- [`_WKCustomHeaderFields.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKCustomHeaderFields.mm#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
