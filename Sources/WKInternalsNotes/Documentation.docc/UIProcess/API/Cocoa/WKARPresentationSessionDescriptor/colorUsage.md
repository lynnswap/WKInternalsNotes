# ``WKInternalsNotes/WKARPresentationSessionDescriptor/colorUsage``

描画用カラーのテクスチャ用途を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite) MTLTextureUsage colorUsage;
```

## Default Value
初期値は `MTLTextureUsageRenderTarget | MTLTextureUsageShaderRead`。

## Discussion
`init` で `MTLTextureUsageRenderTarget | MTLTextureUsageShaderRead` に設定される。

## References
- [`WKARPresentationSession.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L41)
- [`WKARPresentationSession.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L70)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
