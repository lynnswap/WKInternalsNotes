# ``WKInternalsNotes/WKContentView/spatialTrackingLabel``

空間トラッキング用ラベルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) const String& spatialTrackingLabel;
```

## Default Value
`_spatialTrackingLabel` を返す。

## Discussion
`HAVE(SPATIAL_TRACKING_LABEL)` のとき `_spatialTrackingLabel` を返す。

## References
- [`WKContentView.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L69)
- [`WKContentView.mm#L791`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L791)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
