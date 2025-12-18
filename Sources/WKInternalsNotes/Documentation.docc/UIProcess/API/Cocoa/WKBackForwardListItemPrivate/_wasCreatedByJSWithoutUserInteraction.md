# ``WKInternalsNotes/WKBackForwardListItem/_wasCreatedByJSWithoutUserInteraction``

JavaScript によるユーザー操作なし生成かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _wasCreatedByJSWithoutUserInteraction WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
基になる `WebBackForwardListItem` のフラグ値。

## Discussion
内部の `WebBackForwardListItem` が持つフラグを返す。このフラグは back/forward の移動時に、ユーザー操作なしで追加された項目をスキップする判定に使われる。

## References
- [`WKBackForwardListItemPrivate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListItemPrivate.h#L34)
- [`WKBackForwardListItem.mm#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListItem.mm#L93)
- [`WebBackForwardList.cpp#L556`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebBackForwardList.cpp#L556)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
