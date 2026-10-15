/**
 * MARTINA TAGLIETTI — PORTFOLIO GRAFICO 2026
 * Interactive Engine: Lightbox, Flipbook, Vertex Live Preview & Filter System
 */

document.addEventListener('DOMContentLoaded', () => {

    /* ==========================================================================
       1. STICKY HEADER & SCROLL BEHAVIOR
       ========================================================================== */
    const siteHeader = document.querySelector('.site-header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 30) {
            siteHeader.classList.add('scrolled');
        } else {
            siteHeader.classList.remove('scrolled');
        }
    });

    /* ==========================================================================
       2. PROJECT CATEGORY FILTER SYSTEM
       ========================================================================== */
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    const filterCountEl = document.getElementById('filterCount');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const targetCategory = btn.getAttribute('data-filter');
            let visibleCount = 0;

            projectCards.forEach(card => {
                const cardCategories = card.getAttribute('data-category').split(' ');
                if (targetCategory === 'all' || cardCategories.includes(targetCategory)) {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                    visibleCount++;
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 250);
                }
            });

            if (filterCountEl) {
                filterCountEl.textContent = `${visibleCount} Progetti Visualizzati`;
            }
        });
    });

    /* ==========================================================================
       3. HIGH-RES LIGHTBOX MODAL
       ========================================================================== */
    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxClose = document.getElementById('lightboxClose');

    // Trigger on any image with class 'zoomable' or clickable mockup
    const zoomableImages = document.querySelectorAll('.zoomable, .mockup-screen img, .iphone-screen img, .polaroid-showcase-box img, .instagram-mockup-box img, .feature-preview-card img');

    zoomableImages.forEach(img => {
        img.style.cursor = 'zoom-in';
        img.addEventListener('click', (e) => {
            e.stopPropagation();
            const src = img.getAttribute('src');
            const title = img.getAttribute('alt') || 'Tavola Grafica ad Alta Risoluzione';
            
            lightboxImg.src = src;
            lightboxTitle.textContent = title;
            lightboxModal.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
    });

    const closeLightbox = () => {
        lightboxModal.classList.remove('open');
        document.body.style.overflow = '';
    };

    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    if (lightboxModal) {
        lightboxModal.addEventListener('click', (e) => {
            if (e.target === lightboxModal) closeLightbox();
        });
    }

    /* ==========================================================================
       4. VERTEX STUDIO LIVE PREVIEW MODAL
       ========================================================================== */
    const previewModal = document.getElementById('previewModal');
    const previewIframe = document.getElementById('previewIframe');
    const previewTitle = document.getElementById('previewTitle');
    const previewClose = document.getElementById('previewClose');
    const openNewTabBtn = document.getElementById('openNewTabBtn');
    const deviceBtns = document.querySelectorAll('.device-btn');
    const clientChipBtns = document.querySelectorAll('.client-chip-btn');

    let currentClientUrl = 'assets/vertex/gym.html';

    const openPreview = (url, name) => {
        currentClientUrl = url;
        previewIframe.src = url;
        previewTitle.textContent = `Live Preview — ${name}`;
        openNewTabBtn.href = url;
        previewModal.classList.add('open');
        document.body.style.overflow = 'hidden';
    };

    clientChipBtns.forEach(chip => {
        chip.addEventListener('click', () => {
            clientChipBtns.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');

            const url = chip.getAttribute('data-url');
            const name = chip.getAttribute('data-name');
            openPreview(url, name);
        });
    });

    const triggerPreviewBtns = document.querySelectorAll('.btn-launch-preview');
    triggerPreviewBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const url = btn.getAttribute('data-url') || 'assets/vertex/gym.html';
            const name = btn.getAttribute('data-name') || 'Vertex Studio';
            openPreview(url, name);
        });
    });

    // Device Frame Switcher (Desktop / Tablet / Mobile)
    deviceBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            deviceBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const device = btn.getAttribute('data-device');
            previewIframe.className = `preview-iframe ${device}`;
        });
    });

    const closePreview = () => {
        previewModal.classList.remove('open');
        previewIframe.src = 'about:blank';
        document.body.style.overflow = '';
    };

    if (previewClose) previewClose.addEventListener('click', closePreview);
    if (previewModal) {
        previewModal.addEventListener('click', (e) => {
            if (e.target === previewModal) closePreview();
        });
    }

    /* ==========================================================================
       5. 9-PAGE OFFICIAL PORTFOLIO FLIPBOOK / VIEWER
       ========================================================================== */
    const flipbookImg = document.getElementById('flipbookImg');
    const flipbookPageLabel = document.getElementById('flipbookPageLabel');
    const flipbookPrev = document.getElementById('flipbookPrev');
    const flipbookNext = document.getElementById('flipbookNext');
    const thumbItems = document.querySelectorAll('.thumb-item');

    const portfolioPages = [
        { index: 1, title: "Tavola 01 — Copertina Grafica & Titolo Tipografico", file: "assets/pdf_pages/page_1.png" },
        { index: 2, title: "Tavola 02 — Chi Sono: Martina Taglietti (Bio & Passioni)", file: "assets/pdf_pages/page_2.png" },
        { index: 3, title: "Tavola 03 — Progetto Digitale CPME: Soundground (Figma)", file: "assets/pdf_pages/page_3.png" },
        { index: 4, title: "Tavola 04 — Identità Visiva & Manuale Logo: Camelia", file: "assets/pdf_pages/page_4.png" },
        { index: 5, title: "Tavola 05 — Prototipo Web & Mobile: DGM Motori", file: "assets/pdf_pages/page_5.png" },
        { index: 6, title: "Tavola 06 — Progetto Accademico: Forme Essenziali (Artigiani)", file: "assets/pdf_pages/page_6.png" },
        { index: 7, title: "Tavola 07 — Reportage & Set Fotografico Officina (Reflex)", file: "assets/pdf_pages/page_7.png" },
        { index: 8, title: "Tavola 08 — UI/UX Design & Prototipazione: Vertex Studio", file: "assets/pdf_pages/page_8.png" },
        { index: 9, title: "Tavola 09 — Contatti & Network Professionale", file: "assets/pdf_pages/page_9.png" }
    ];

    let currentPageIdx = 0;

    const renderFlipbookPage = (idx) => {
        if (idx < 0) idx = portfolioPages.length - 1;
        if (idx >= portfolioPages.length) idx = 0;
        currentPageIdx = idx;

        const current = portfolioPages[currentPageIdx];
        flipbookImg.style.opacity = '0.3';
        
        setTimeout(() => {
            flipbookImg.src = current.file;
            flipbookImg.alt = current.title;
            flipbookPageLabel.textContent = `${current.title} (${currentPageIdx + 1} di 9)`;
            flipbookImg.style.opacity = '1';
        }, 120);

        thumbItems.forEach((t, i) => {
            if (i === currentPageIdx) {
                t.classList.add('active');
                t.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            } else {
                t.classList.remove('active');
            }
        });
    };

    if (flipbookPrev) flipbookPrev.addEventListener('click', () => renderFlipbookPage(currentPageIdx - 1));
    if (flipbookNext) flipbookNext.addEventListener('click', () => renderFlipbookPage(currentPageIdx + 1));

    thumbItems.forEach((thumb, i) => {
        thumb.addEventListener('click', () => renderFlipbookPage(i));
    });

    /* Keyboard navigation */
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeLightbox();
            closePreview();
        }
        if (lightboxModal && !lightboxModal.classList.contains('open') && previewModal && !previewModal.classList.contains('open')) {
            if (e.key === 'ArrowLeft') renderFlipbookPage(currentPageIdx - 1);
            if (e.key === 'ArrowRight') renderFlipbookPage(currentPageIdx + 1);
        }
    });

    /* ==========================================================================
       6. TOAST NOTIFICATIONS & COPY TO CLIPBOARD
       ========================================================================== */
    const toast = document.getElementById('toastMsg');
    const toastText = document.getElementById('toastText');
    let toastTimeout = null;

    const showToast = (message) => {
        if (toastTimeout) clearTimeout(toastTimeout);
        toastText.textContent = message;
        toast.classList.add('show');
        toastTimeout = setTimeout(() => {
            toast.classList.remove('show');
        }, 3200);
    };

    const copyBtns = document.querySelectorAll('.copy-trigger');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const copyValue = btn.getAttribute('data-copy');
            if (copyValue) {
                navigator.clipboard.writeText(copyValue).then(() => {
                    showToast(`Copiato: ${copyValue}`);
                }).catch(() => {
                    showToast(`Valore: ${copyValue}`);
                });
            }
        });
    });

    /* ==========================================================================
       7. CONTACT FORM SUBMISSION HANDLER
       ========================================================================== */
    const contactForm = document.getElementById('portfolioContactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = contactForm.querySelector('.btn-submit-form');
            const originalContent = submitBtn.innerHTML;

            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Invio in corso...';
            submitBtn.disabled = true;

            setTimeout(() => {
                submitBtn.innerHTML = '<i class="fas fa-check"></i> Messaggio Inviato con Successo!';
                submitBtn.style.backgroundColor = '#10B981';
                showToast("Grazie per il tuo messaggio! Ti risponderò al più presto.");
                contactForm.reset();

                setTimeout(() => {
                    submitBtn.innerHTML = originalContent;
                    submitBtn.style.backgroundColor = '';
                    submitBtn.disabled = false;
                }, 3500);
            }, 900);
        });
    }

    /* ==========================================================================
       8. MOBILE NAVIGATION DRAWER
       ========================================================================== */
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.querySelector('.nav-menu');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('open-mobile');
            mobileToggle.classList.toggle('open');
        });

        // Close on link click
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('open-mobile');
                mobileToggle.classList.remove('open');
            });
        });
    }

});
