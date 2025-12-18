# ``WKInternalsNotes/WKBackForwardList/_clear()``

現在の項目を残して他の履歴アイテムを削除する。

## Objective-C Declaration
```objective-c
- (void)_clear;
```

## Discussion
`WebBackForwardList::clear` に委譲し、現在項目以外を削除して `m_currentIndex` を 0 に更新する。ページが無い場合や履歴が 1 件以下の場合は何もしない。

## References
- [`WKBackForwardListPrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListPrivate.h#L33)
- [`WKBackForwardList.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardList.mm#L101)
- [`WebBackForwardList.cpp#L406`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebBackForwardList.cpp#L406)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
