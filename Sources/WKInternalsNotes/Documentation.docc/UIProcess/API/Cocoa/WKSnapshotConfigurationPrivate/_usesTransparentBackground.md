# ``WKInternalsNotes/WKSnapshotConfiguration/_usesTransparentBackground``

スナップショットで透明背景を使うかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUsesTransparentBackground:) BOOL _usesTransparentBackground WK_API_AVAILABLE(macos(14.2), ios(17.2));
```

## Default Value
初期値は NO（`init` で設定されず ivar のゼロ初期化）。

## Discussion
getter は `_usesTransparentBackground` を返し、setter は ivar を更新する。

## References
- [`WKSnapshotConfigurationPrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfigurationPrivate.h#L36)
- [`WKSnapshotConfiguration.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfiguration.mm#L36)
- [`WKSnapshotConfiguration.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfiguration.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
