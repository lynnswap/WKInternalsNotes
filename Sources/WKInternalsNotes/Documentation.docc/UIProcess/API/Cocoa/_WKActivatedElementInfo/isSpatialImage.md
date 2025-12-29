# ``WKInternalsNotes/_WKActivatedElementInfo/isSpatialImage``

空間画像かどうかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isSpatialImage WK_API_AVAILABLE(visionos(2.2));
```

## Default Value
`NO`（初期化時に設定される）。

## Discussion
`ENABLE(SPATIAL_IMAGE_DETECTION)` の場合に `InteractionInformationAtPosition` の `isSpatialImage` を保持して返す。

## References
- [`_WKActivatedElementInfo.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L52)
- [`_WKActivatedElementInfo.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
