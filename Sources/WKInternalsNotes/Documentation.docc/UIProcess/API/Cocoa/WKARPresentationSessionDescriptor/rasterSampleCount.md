# ``WKInternalsNotes/WKARPresentationSessionDescriptor/rasterSampleCount``

ラスタのサンプル数を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite) NSUInteger rasterSampleCount;
```

## Default Value
初期値は `1`。

## Discussion
`init` で `1` に設定される。

## References
- [`WKARPresentationSession.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L42)
- [`WKARPresentationSession.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L70)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
