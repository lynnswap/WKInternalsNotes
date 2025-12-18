# ``WKInternalsNotes/WKBackForwardListItem/_copySnapshotForTesting()``

スナップショットがある場合に CGImageRef を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (CGImageRef)_copySnapshotForTesting WK_API_AVAILABLE(macos(10.12.3), ios(10.3));
```

## Discussion
内部の `snapshot()` が存在する場合は `asImageForTesting()` の結果を返し、スナップショットが無い場合は `nullptr` を返す。

## References
- [`WKBackForwardListItemPrivate.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListItemPrivate.h#L31)
- [`WKBackForwardListItem.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListItem.mm#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
