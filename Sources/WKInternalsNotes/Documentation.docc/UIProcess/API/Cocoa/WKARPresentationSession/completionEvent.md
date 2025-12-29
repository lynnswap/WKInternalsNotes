# ``WKInternalsNotes/WKARPresentationSession/completionEvent``

Metal の共有イベントを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nonnull, retain, readonly) id<MTLSharedEvent> completionEvent;
```

## Default Value
`_loadMetal` で生成した `id<MTLSharedEvent>`。

## Discussion
`_loadMetal` で `newSharedEvent` を作成し、getter で返す。

## References
- [`WKARPresentationSession.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L187)
- [`WKARPresentationSession.mm#L350`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L350)
- [`WKARPresentationSession.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L50)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
