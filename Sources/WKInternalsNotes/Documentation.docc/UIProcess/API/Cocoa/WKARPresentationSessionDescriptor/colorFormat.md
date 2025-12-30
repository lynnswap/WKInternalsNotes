# ``WKInternalsNotes/WKARPresentationSessionDescriptor/colorFormat``

描画用カラーのピクセル形式を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite) MTLPixelFormat colorFormat;
```

## Default Value
初期値は `MTLPixelFormatBGRA8Unorm_sRGB`。

## Discussion
`init` で `MTLPixelFormatBGRA8Unorm_sRGB` に設定される。

## References
- [`WKARPresentationSession.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L40)
- [`WKARPresentationSession.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L70)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
