# ``WKInternalsNotes/WKBackForwardList/_removeAllItems()``

履歴リストの全アイテムを削除する。

## Objective-C Declaration
```objective-c
- (void)_removeAllItems;
```

## Discussion
`WebBackForwardList::removeAllItems` に委譲し、全エントリを除去して `m_currentIndex` を `nullopt` にする。その後、空のリストとして `didChangeBackForwardList` を通知する。

## References
- [`WKBackForwardListPrivate.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListPrivate.h#L30)
- [`WKBackForwardList.mm#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardList.mm#L96)
- [`WebBackForwardList.cpp#L393`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebBackForwardList.cpp#L393)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
