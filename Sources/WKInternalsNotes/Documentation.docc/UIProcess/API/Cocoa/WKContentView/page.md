# ``WKInternalsNotes/WKContentView/page``

対応する `WebPageProxy` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebPageProxy* page;
```

## Default Value
`_page.get()` を返す。

## Discussion
内部に保持している `WebPageProxy` をそのまま返す getter。

## References
- [`WKContentView.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L56)
- [`WKContentView.mm#L543`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L543)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
