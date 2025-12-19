# ``WKInternalsNotes/WKBackForwardListItem/_item``

ラップしている WebBackForwardListItem への参照を返す。

## Objective-C Declaration
```objective-c
@property (readonly) WebKit::WebBackForwardListItem& _item;
```

## Default Value
インスタンスが保持する `WebBackForwardListItem`。

## Discussion
内部の `AlignedStorage<WebBackForwardListItem>` に格納された値を参照として返す。`WKBackForwardListItem` のラッパー実装で利用される内部アクセサ。

## References
- [`WKBackForwardListItemInternal.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListItemInternal.h#L41)
- [`WKBackForwardListItem.mm#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListItem.mm#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
