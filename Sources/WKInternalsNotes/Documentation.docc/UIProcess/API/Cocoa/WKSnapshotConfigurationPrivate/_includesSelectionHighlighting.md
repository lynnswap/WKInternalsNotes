# ``WKInternalsNotes/WKSnapshotConfiguration/_includesSelectionHighlighting``

スナップショットに選択ハイライトを含めるかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setIncludesSelectionHighlighting:) BOOL _includesSelectionHighlighting WK_API_AVAILABLE(macos(13.3));
```

## Default Value
`init` で YES に設定される。

## Discussion
getter は `_includesSelectionHighlighting` を返し、setter は ivar を更新する。

## References
- [`WKSnapshotConfigurationPrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfigurationPrivate.h#L33)
- [`WKSnapshotConfiguration.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfiguration.mm#L33)
- [`WKSnapshotConfiguration.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfiguration.mm#L33)
- [`WKSnapshotConfiguration.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfiguration.mm#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
