# ``WKInternalsNotes/WKApplicationStateTrackingView/isBackground``

`ApplicationStateTracker` の背景状態を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isBackground;
```

## Default Value
`_applicationStateTracker` が無い場合は `YES`。

## Discussion
`_applicationStateTracker` が存在すれば `isInBackground()` を返し、なければ `YES` を返す。

## References
- [`WKApplicationStateTrackingView.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKApplicationStateTrackingView.h#L36)
- [`WKApplicationStateTrackingView.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKApplicationStateTrackingView.mm#L139)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
