# ``WKInternalsNotes/_WKSpatialBackdropSource/initWithSpatialBackdropSource(_:)``

`SpatialBackdropSource` から初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSpatialBackdropSource:(const WebCore::SpatialBackdropSource&) spatialBackdropSource;
```

## Discussion
`m_sourceURL` / `m_modelURL` をコピーして保持し、`m_environmentMapURL` があれば設定する。

## References
- [`_WKSpatialBackdropSourceInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSpatialBackdropSourceInternal.h#L35)
- [`_WKSpatialBackdropSource.mm#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSpatialBackdropSource.mm#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
