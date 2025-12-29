# ``WKInternalsNotes/WKARPresentationSession/colorTexture``

現在の描画先テクスチャを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, retain, readonly) id<MTLTexture> colorTexture;
```

## Default Value
`startFrame` で取得した drawable の `texture`。

## Discussion
`_currentDrawable` の `texture` を返す。`startFrame` が成功していない場合は `nil`。

## References
- [`WKARPresentationSession.mm#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L191)
- [`WKARPresentationSession.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L195)
- [`WKARPresentationSession.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
