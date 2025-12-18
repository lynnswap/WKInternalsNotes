# ``WKInternalsNotes/WKSnapshotConfiguration/_usesContentsRect``

contentsRect を使用するかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUsesContentsRect:) BOOL _usesContentsRect WK_API_AVAILABLE(macos(15.0));
```

## Default Value
`init` で NO に設定される。

## Discussion
getter は `_usesContentsRect` を返し、setter は ivar を更新する。

## References
- [`WKSnapshotConfigurationPrivate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfigurationPrivate.h#L38)
- [`WKSnapshotConfiguration.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfiguration.mm#L51)
- [`WKSnapshotConfiguration.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfiguration.mm#L91)
- [`WKSnapshotConfiguration.mm#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSnapshotConfiguration.mm#L96)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
